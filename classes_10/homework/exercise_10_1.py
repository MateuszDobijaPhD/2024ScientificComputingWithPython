# # EXERCISE 10.1 (VENV)
# #
# # Create a virtual environment for this course using 'venv' or 'virtualenv'. Install numpy, matplotlib, pandas. Send me a list of commands used (with outputs).
#
# Commands list:
# 1) python -m venv exercise10VEnv        #utworzenie venv
#
# (venv) PS D:\obliczenia_naukowe_w_jezyku_python\classes_10\homework> python -m venv exercise10VEnv
# (venv) PS D:\obliczenia_naukowe_w_jezyku_python\classes_10\homework>
#
# 2) ./exercise10VEnv/Scripts/activate    #aktywacja wirtualnego srodowiska
#
# (venv) PS D:\obliczenia_naukowe_w_jezyku_python\classes_10\homework> ./exercise10VEnv/Scripts/activate
# (exercise10VEnv) PS D:\obliczenia_naukowe_w_jezyku_python\classes_10\homework> pip install numpy
#
#
# 3) pip install numpy
#
# (exercise10VEnv) PS D:\obliczenia_naukowe_w_jezyku_python\classes_10\homework> pip install numpy
# Collecting numpy
#   Downloading numpy-1.26.4-cp39-cp39-win_amd64.whl (15.8 MB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.8/15.8 MB 20.5 MB/s eta 0:00:00
# Installing collected packages: numpy
# Successfully installed numpy-1.26.4
# WARNING: You are using pip version 22.0.4; however, version 24.0 is available.
# You should consider upgrading via the 'D:\obliczenia_naukowe_w_jezyku_python\classes_10\homework\exercise10VEnv\Scripts\python.exe -m pip install --upgrade pip' command.
#
#
# 3) pip install matplotlib
#
# (exercise10VEnv) PS D:\obliczenia_naukowe_w_jezyku_python\classes_10\homework> pip install matplotlib
# Collecting matplotlib
#   Downloading matplotlib-3.8.4-cp39-cp39-win_amd64.whl (7.7 MB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.7/7.7 MB 20.4 MB/s eta 0:00:00
# Collecting pillow>=8
#   Downloading pillow-10.3.0-cp39-cp39-win_amd64.whl (2.5 MB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 MB 14.7 MB/s eta 0:00:00
#   Downloading fonttools-4.51.0-cp39-cp39-win_amd64.whl (2.2 MB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 23.4 MB/s eta 0:00:00
# Collecting cycler>=0.10
#   Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
# Collecting zipp>=3.1.0
#   Downloading zipp-3.18.1-py3-none-any.whl (8.2 kB)
# Collecting six>=1.5
#   Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
# Installing collected packages: zipp, six, pyparsing, pillow, packaging, kiwisolver, fonttools, cycler, contourpy, python-dateutil, importlib-resources, matplotlib
# Successfully installed contourpy-1.2.1 cycler-0.12.1 fonttools-4.51.0 importlib-resources-6.4.0 kiwisolver-1.4.5 matplotlib-3.8.4 packaging-24.0 pillow-10.3.0 pyparsing-3.1.2 python-dateutil-2.9.0.post0 six-1.16.0 zipp-3.18.1
# WARNING: You are using pip version 22.0.4; however, version 24.0 is available.
# You should consider upgrading via the 'D:\obliczenia_naukowe_w_jezyku_python\classes_10\homework\exercise10VEnv\Scripts\python.exe -m pip install --upgrade pip' command.
#
#
# 4) pip install pandas
#
# (exercise10VEnv) PS D:\obliczenia_naukowe_w_jezyku_python\classes_10\homework> pip install pandas
# Collecting pandas
#   Using cached pandas-2.2.2-cp39-cp39-win_amd64.whl (11.6 MB)
# Requirement already satisfied: tzdata>=2022.7 in d:\obliczenia_naukowe_w_jezyku_python\classes_10\homework\exercise10venv\lib\site-packages (from pandas) (2024.1)
# Requirement already satisfied: pytz>=2020.1 in d:\obliczenia_naukowe_w_jezyku_python\classes_10\homework\exercise10venv\lib\site-packages (from pandas) (2024.1)
# Requirement already satisfied: python-dateutil>=2.8.2 in d:\obliczenia_naukowe_w_jezyku_python\classes_10\homework\exercise10venv\lib\site-packages (from pandas) (2.9.0.post0)
# Requirement already satisfied: numpy>=1.22.4 in d:\obliczenia_naukowe_w_jezyku_python\classes_10\homework\exercise10venv\lib\site-packages (from pandas) (1.26.4)
# Requirement already satisfied: six>=1.5 in d:\obliczenia_naukowe_w_jezyku_python\classes_10\homework\exercise10venv\lib\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)
# Installing collected packages: pandas
# Successfully installed pandas-2.2.2
# WARNING: You are using pip version 22.0.4; however, version 24.0 is available.
# You should consider upgrading via the 'D:\obliczenia_naukowe_w_jezyku_python\classes_10\homework\exercise10VEnv\Scripts\python.exe -m pip install --upgrade pip' command.
