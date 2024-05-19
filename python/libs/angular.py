import os
import subprocess

def create_angular_project(args):
    
    project_path = f'{args.dir}/{args.name}'

    os.makedirs(project_path, exist_ok=True)

    ng_new = f'ng new {args.name} --inline-style --package-manager=pnpm --prefix=fwks --routing --skip-git --skip-install --strict --standalone --style=scss'
    subprocess.run(ng_new, shell=True, capture_output=True, text=True, cwd=args.dir)
    
    for dir in [
        'abstractions', 
        'components', 
        'directives', 
        'functions', 
        'guards', 
        'pipes', 
        'providers', 
        'services' ]:
        create_dir(f'{project_path}/src/app/core/{dir}')

    create_dir(f'{project_path}/src/app/pages')
    
    # add tsconfig lines
    
    # add tailwind, postcss and autoprefixer packages
    
    # init tailwind config
    
    # add tailwind init files

    # print(f'project name: {args.name}\nproject type: {args.type}\nproject directory output: {args.dir}')

def create_dir(path, index=True):
    os.makedirs(path, exist_ok=True)
    if index:
        with open(f'{path}/index.ts', 'w'):
            pass