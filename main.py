#! usr/bin/env python
import sys 
import argparse
import logging

version = "CAPRA v0.0.0"
verbosity = 1

def main(argv):
    print version
    parser = argparse.ArgumentParser(epilog="""Visit www.github.com/gummywormz/CAPRA
                                     for more documentation and tutorials.""",
                                     description="A random file distributor")


    parser.add_argument("--version", action="version", version=version)
    
    parser.add_argument("-v", "--verbose",default=1, type=int,
                        help="""Changes verbosity level. 0 is quiet, 1 is standard (errors only),
                        2 is warnings, 3 is debugging"""
                        ,choices=[0,1,2,3])
    

    
    parser.add_argument("directory", help="""Directory of assignments. You only
						need the name of the folder itself.(i.e. My Drive/Classroom 
						becomes just Classroom) If you have multiple folders 
						of the same name, use id instead""")
    
    #each assignment is stored in its own folder...
    #parser.add_argument("assignment_name",required=True, help="""File name of the 
    #                   assignment to get (not including student's name if it has one)""")
    
    group = parser.add_mutually_exclusive_group(required=True)
    
    group.add_argument("-l","--local-directory",action="store_true",
                        help="Specifies that the directory is local")
                        
    group.add_argument("-d","--drive-directory",action="store_true",
                        help="Specifies that the directory is on Google Drive")
                        
    group.add_argument("-i","--directory-id",action="store_true",
                        help="Specifies that the directory is Google Drive ID")
                        
    parser.add_argument("-c","--clear-output", action="store_true",
                        help="""Deletes all files downloaded if a Google Drive 
                        option is specified (-d or -i)""")
                        
    parser.add_argument("-o","--output-directory", help="""Full path of directory 
                        to download files to if a Google Drive option is specified
                        (defaults to a new local directory with the assignment name)"""
                        )
                        
    parser.add_argument("-t", "--type",help="""The file type to download the Google
                        Doc as if a Google Drive option is specified.(default is pdf)""",
                        choices=["pdf","html","docx"],default="pdf")
                        
    parser.add_argument("-x","--companionate-folder",help="""Any files in this 
                        folder will also be distributed. Directory must be local.""")
                        
    parser.add_argument("-e", "--email-list",help="""List of emails to distribute
                        files to. Required if local directory is specified. 
                        (either csv or separated by new lines)""")
                        
    args = parser.parse_args()
    
    if args.local_directory and not args.email_list:
        print "You specified a local directory but no list of emails to send the",
        print "files to!"
        sys.exit(2)
    
    if args.verbose:
        verbosity = args.verbose
        
    logging_level = -1
    
    if verbosity = 1:
        logging_level = logging.ERROR
    elif verbosity = 2:
        logging_level = logging.WARNING
    elif verbosity = 3:
        logging_level = logging.DEBUG
    else:
        logging_level = logging.CRITICAL
		
	logging.basicConfig(level = logging_level,format="%Levelname)s: %(message)s")

if __name__ == "__main__":
    main(sys.argv)