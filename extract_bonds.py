import os,sys
import subprocess

import argparse
parser = argparse.ArgumentParser(
	formatter_class=argparse.RawDescriptionHelpFormatter,
	description=('''\
                    Handy-Dandy 
                   Bond Extractor
            ------------------------------
              Extracts bonds that atoms
              in "sele" are involved in
             and outputs them to "output"
	'''))

parser.add_argument('--prmtop', type=str, 
help="The prmtop file for the system in question")
parser.add_argument('--inpcrd', type=str,
help="The inpcrd file for the system in question")
parser.add_argument('--sele', type=str,
help="The selection for interest atoms; defaults to 'backbone'",
default='backbone')
parser.add_argument('--output', type=str,default=sys.stdout,
help="Where the list of bonds will be written to; defaults to stdout")
parser.add_argument('--tcl_script_name', type=str,
help="Name of the temporary script we'll be using; new files only!")
parser.add_argument('--nocleanup', action='store_true', default=False,
help="if you don't want the tcl script to be deleted after usage.")

args = parser.parse_args()

#Check if the args.tcl_script_name file already exists, so we don't
#overwrite anything the user might need

if(os.path.isfile(args.tcl_script_name) == True):
	print(f'Error: There is already a file called {args.tcl_script_name}. Exiting...')
	sys.exit()

#Write the temp script that VMD uses next
temp_script = open(args.tcl_script_name, "w")
temp_script.write(
"#load protein from prmtop and inpcrd\nmol new " +
 str(args.prmtop) + "\nmol addfile " + str(args.inpcrd) +
 " type rst7\natomselect 0 " + '"' + str(args.sele) + '"' +
 "\nset bonds   [atomselect0 getbonds]\nset indexes" +
 " [atomselect0 list]\nset outputID [open " + str(args.output) +
 " w]\nfor {set i 0} {$i < [llength $indexes]} {incr i}" +
 " {\nset nob [llength [lindex $bonds $i]]\nfor {set j 0}" +
 " {$j < $nob} {incr j} {\nputs $outputID " +
 '"[lindex $indexes $i] [lindex [lindex $bonds $i] $j]"' + "\n}\n}\nclose $outputID\nexit")

temp_script.close()

#run VMD with the script we just wrote

procstr = ['vmd', '-dispdev', 'none', '-e', args.tcl_script_name]
proc = subprocess.Popen(procstr, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
proc.communicate()

#now we just cleanup by deleting the script we used
if args.nocleanup==False:
	subprocess.call(['rm', args.tcl_script_name])
	print("Done!")
