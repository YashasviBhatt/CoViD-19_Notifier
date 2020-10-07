# CoViD-19 Notifier
This Project fetch the **Real Time CoViD-19 status of India** from **[Ministry of Health and Family Welfare Website](https://www.mohfw.gov.in/)** and display it as _Notification_ to user. Since, the data is from **MOHFW**, thus doubts regarding accuracy doesn't exists i.e it is 100% accurate as per the Government and it's affiliated Agencies who manage this Issue.
## To run this Project please follow these steps

1. Open _command prompt_ or _powershell window_.
2. Type this command<br>`git clone https://github.com/YashasviBhatt/CoViD-19_Notifier`<br>and press enter.
3. Go inside the _Cloned Repository_ folder and open _command-prompt_ or _powershell window_.

4. Type<br>`pip install -r requirements.txt`<br> and press enter in either _command_prompt_ or _powershell window_ as _administrator_.
5. After Installing all the required _libraries_ execute the program<br>`python CoViD_19_Notifier.py`.
6. If you would like to see the _data_ which showed up then open **data.csv** file.

### Working
1. Firstly, we have created a **function** named as `notifyMe(title, message)` which will generate a notification with `title` and `message` _passed_ as `arguments`.
2. Secondly, we have created a **function** named as `getData(url)` which will fetch the data from url and returns the text it extracted from url.
3. Now, we have _parsed_ the website of **[Ministry of Health and Family Welfare](https://www.mohfw.gov.in/)**
using `Beautiful Soup HTML Parser`.
4. `Beautiful Soup` parse the website and generate a **parse tree** for _parsed pages_, thus this _parse tree_ is then used for _data extraction_.
5. After _parsing_ the Website we have extracted the _useful/required data_ using several `Beautiful Soup` features and passed them to `notifyMe(title, message)` as arguments, which will _lastly_ generate **notification**.
