from Operation import operation as op

print('______________File Manager_______________')


default_path= f'/home/{op.os.getenv('USER')}/'
pathIndecator = '~'
op.cd(default_path)
while True:
    command = input(f'{pathIndecator}$ ')   # For showing the current path as prefix  before input like if cwd is /home it shows '/home$ '
    filepath= command.split(' ')
    if filepath[0] == 'cd':
        try:
            status=op.cd(filepath[1])
            if status.startswith(f'{default_path}'):
                temp = status.split(default_path)
                pathIndecator = f'~{temp[-1]}'
                continue
            else:
                pathIndecator = status
                continue
        except IndexError:
            status=op.cd(f'{default_path}')
            pathIndecator = '~'
            continue
        except FileNotFoundError:
            if len(filepath) >2:
                print(f'python: cd: too many aruments') 
                continue   
            elif filepath[-1] == '~':
                status=op.cd(f'{default_path}')
                pathIndecator = '~'
                continue
            else:
                print(f'cd: {filepath[-1]}: No such file or directory')
        except PermissionError:
            print('python: this need root access.')
    elif filepath[0] == 'ls':
        try:
            if filepath[1] == '-a':
                files = op.ls(filepath[2])
                for i in files:
                    print(i)
            else:
                files =op.ls(filepath[1])
                for i in files:
                    if not i.startswith('.'):
                        print(i)

        except IndexError:
            files = op.ls(op.pwd()) 
            for i in files:
                if '-a' in filepath:
                    print(i)
                else:
                    if not i.startswith('.'):
                        print(i)
        except FileNotFoundError:
            if 'ls' and '-a' in command:
                print(f'python: {filepath[2]}:  no such file or direcory')
            else:
                print(f'python: {filepath[1]}:  no such file or direcory')                
        except PermissionError:
            print('python: this need root access.')
    elif filepath[0] == 'pwd':
        try:
            print(op.pwd())
            continue
        except OSError:
            print('Something is wrong in this filesystem')
        except FileNotFoundError:
            print(f'python: {filepath[1]}: no such directory ')
        except PermissionError:
            print('Need root permission for this. Run the program using sudo.')    
    elif filepath[0] == 'mkdir':
        try:
            if not '-p' in filepath: 
                for i in filepath[1:]:
                    op.create(i)
            else:
                for i in filepath[2:]:
                    op.os.makedirs(i)
        except FileExistsError:
            print(f'mkdir: cannot create directory {filepath[1]}: File exists')
        except FileNotFoundError:
                print(f'mkdir: cannot create directory {filepath[1]}: No such file or directory \n\t use -p to make recuresive directory.')
        except PermissionError:
            print('python: this need root access.')  
        # except:
        #     if '-p' in filepath:
        #         op.os.makedirs(filepath[-1])        
    elif filepath[0] == 'touch':
        try:
            for i in filepath[1:]:
                with open(i,'x'):
                    pass
        except FileNotFoundError:
            print(f'touch: cannot touch {filepath[1]}: No such file or directory')
        except FileExistsError:
            if '-f' in filepath:
                for i in filepath[2:]:
                    with open(i,'w') as f:
                        f.write('')
                    
            else:
                print(f'File exists: {filepath[1]}\n \tto replace use -f')
    elif filepath[0] == 'rm':
        try:
            if op.os.path.isfile(filepath[1]):
                for i in filepath[1:]:
                    op.os.remove(i)
            # elif op.os.path.isdir(filepath[2]):
            else:
                if '-r' in filepath or '-rf' in filepath:
                    for i in filepath[2:]:
                        op.delete(i)    
        except IndexError:
                print(f'rm: cannot remove {filepath[1]}: Is a directory\n\t user -r to delete.')
        except FileNotFoundError:
            print(f'rm: cannot remove {filepath[1]}: No such file or directory')
        except OSError:
            if '-rf' in filepath:
                for i in filepath[2:]:
                    op.shutil.rmtree(i)
            else:
                print(f'rm: cannot remove {filepath[-1]}: Is a non empty directory\n\t use -rf to delete.')
    
    elif filepath[0] == 'cp':
        try:
            if op.os.path.isfile(filepath[1]):
                op.copyfile(filepath[-2],filepath[-1])
            else:
                op.copydir(filepath[-2],filepath[-1])
        except FileNotFoundError:
            print(f'cp: cannot copy {filepath[-2]}: No such file or directory')
    elif filepath[0] =='mv':
        try:
            op.movefile(filepath[-2],filepath[-1])
        except FileNotFoundError:
            print(f'mv: cannot copy {filepath[-2]}: No such file or directory')
        # except FileExistsError:
        #     for i in 


    else:
        print(f'python: {command}: command not found....')