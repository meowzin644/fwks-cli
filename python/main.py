import argparse
import os
from libs.angular import create_angular_project

if __name__ == '__main__':
    try:
        
        parser = argparse.ArgumentParser(description='fwks CLI - fwks Command Line Interface')

        parser.add_argument('name', help='Project name')
        parser.add_argument('-t', '--type', default='angular', help='Type of the project; [angular, dotnet]')
        parser.add_argument('-d', '--dir', default=os.getcwd() ,help='Directory output for the new project')

        args = parser.parse_args()

        if args.type == 'angular':
            create_angular_project(args)

    except Exception as ex:
        print('Something happened.', ex)