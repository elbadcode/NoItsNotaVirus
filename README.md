VirusTotal false flags are the bane of many developers, especially in mod communities where people tend to have poor computer literacy and think everyone is out to get them so here is the simplest example possible.

I've written two scripts here. One writes a file called helloworld.txt with the text "Hello World", the other simply prints "Hello World" to console. I compiled the scripts with nuitka as standalone executables which simply means they package the python environment so the end user gets an exe that just works with no requirements. I also compiled the second script without bundling the python environment. Can you guess what will happen when I upload these to virus total?

So our script that writes a file got 17 counts of trojan detection

![image](https://github.com/user-attachments/assets/59b1dd9e-6e70-4e9e-a304-cea449a113dc)

The script that simply prints "Hello World" gets 16 counts

![image](https://github.com/user-attachments/assets/e2b4c2bb-1e5e-4654-8121-518258a067a4)

It seems that trapmine considers any file output to be a virus but otherwise they both got the same reports
![image](https://github.com/user-attachments/assets/b10e06c3-7bd1-4240-a005-59ae52ef668f)

And lastly we have baby's first script without the python environment bundled. 2 reports still, that's enough for some users to refuse to touch it and others may blindly follow suit. Who knows, maybe there's some hidden shell code that will steal your info and upload it back to me

![image](https://github.com/user-attachments/assets/aa33f0e6-3013-4741-b3ec-70526680f9a0)

So its clear that including a python environment will guarantee many false flags even without using any imports.

So does this mean virustotal is useless? No absolutely not, there's a lot of great info you can get from it, but you have to actually read the info, and before even considering uploading a file you should have a good reason to fear malicious code and upon getting the results you should be prepared to READ them. If a user with no previous posts, no links to other socials, a randomly generated name and no profile picture uploads an executable with unclear functions or something that sounds too good to be true then yes by all means upload it. If a user has some post history, has links to other socials, posts source code, and clearly states the purpose of the code, well I can't say with complete certainty that it will be safe, but in 20 years of modding games I've never once downloaded a virus or seen a reputable person upload one so take that as you will

If you're a developer tired of getting questions about false flags feel free to link here

Reports:
https://www.virustotal.com/gui/file/e63b1290a90e6e5dc4677b0f9b9e917e1131cfb9043e6ffa05ea90b061510143?nocache=1
https://www.virustotal.com/gui/file/a48f02749ae5c8df5acbde906d276f13fa0a389cb021e71511a4a5c6770e3ee3?nocache=1
https://www.virustotal.com/gui/file/48217bd5f60cb07af6bfdfec52344034df3cb50d5957afbf0b215745ab257234?nocache=1

