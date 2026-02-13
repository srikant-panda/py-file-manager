from Operation import operation as op

print('______________File Manager_______________')


default_path= '/home/s-fedora/'
pathIndecator = '~'
op.cd(default_path)
while True:
    command = input(f'{pathIndecator}$ ')   # For showing the current path as messanf in before input like if cwd is /home it shows '/home$ '
    filepath= command.split(' ')
    if filepath[0] == 'cd':
        try:
            status=op.cd(filepath[1])
            pathIndecator = status
            continue
        except IndexError:
            pstatus=op.cd('/home/s-fedora/')
        except FileNotFoundError:
            if len(filepath) >2:
                print(f'python: cd: too many aruments')    
            elif filepath[1] == '~':
                status=op.cd('/home/s-fedora/')
            else:
                print(f'cd: {filepath[1]}: No such file or directory')
    elif filepath[0] == 'ls':
        status = op.ls()
        try:
            if filepath[1] == '-a':
                for i in status:
                    print(i)
                continue
        except:
           
            for i in status:
                if not i.startswith('.'):
                    print(i)
                    
    
    else:
        print(f'python: {command}: command not found....')