                                   Lab 2-1: Project 2-1: Using an Online Password Cracker
                                                                        
In this project, you create a digest on a password and then crack it to demonstrate the speed of cracking weak passwords.

●	The first step is to use a general-purpose hash algorithm to create a password hash. Use your web browser to go to www.fileformat.info/tool/hash.htm. (The location of the content on the Internet may change without warning; if you are no longer able to access the program through this URL, use a search engine and search for “Fileformat.info.”)

●	Under String hash, enter the simple password apple123 in the Text: box.

●	Click Hash.

●	Scroll down the page and copy the MD5 hash of this password to your Clipboard by selecting the text, right-clicking it, and choosing Copy.

MD5 Hash for apple123: 75a593a34aa5ba8e5e5788b7c899802e

●	Open a new tab on your web browser.

●	Go to https://crackstation.net/.

●	Paste the MD5 hash of apple123 into the text box below Enter up to 20 non-salted hashes, one per line.

●	In the reCAPTCHA box, click the I ’ m not a robot check box.

●	Click Crack Hashes.

●	How long did it take to crack this hash?

It took less than one second for it to crack the MD5 hash.

●	Click the browser tab to return to FileFormat.Info.

●	Under String hash, enter the longer password applesauce1234 in the Text: box.

●	Click Hash.

MD5 Hash for applesauce1234: 18ff67e7f937a18d89d078ce868b1a19 

●	Scroll down the page and copy the MD5 hash of this password to your Clipboard.

●	Click the browser tab to return to the CrackStation site.

●	Paste the MD5 hash of applesauce1234 into the text box below Enter up to 20 non-salted hashes, one per line.

●	In the reCAPTCHA box, click the I ’ m not a robot check box.

●	Click Crack Hashes.

●	How long did it take this online rainbow table to crack this stronger password hash?

Again, it took the password cracker nearly instantaneous results of the correct password.  

●	Click the browser tab to return to FileFormat.Info and experiment by entering new passwords, computing their hash, and testing them on the CrackStation site. If you are bold, enter a string hash that is similar to a real password that you use.
I tried a fake password similar to the style I use and it came back with a red Type Unknown, Results Not Found. I use a string of randomized letters and numbers in a six-by-three pattern with no discernible words or digits that could give away information such as XXXXXX-XXXXXX-XXXXXX. It has worked for me since changing after learning the bad habits I was creating for my passwords. 
 
●	What does this tell you about the speed of password-cracking tools? What does it tell you about how easy it is for attackers to crack weak passwords? This tells me the algorithms and hashs the banks and other companies use have been broken long ago, how truly exploitable the current system is and how important it is to have personal weaponry such as stronger passwords through using simple rules to keep you safe. I will use the rules of 1) Not using passwords consisting of dictionary words or phonetic words even though when I tried a rather uncouth phrase, albeit with a more intellectual phrasing, 2) I don’t repeat characters or use sequential letters or numbers 3) I don’t use birthdays or family members’ information, addresses, pet names, or any personal information, and 4) I use long passwords with a sequence of randomized letters and numbers in a six-by-three pattern such as ugbk3g-ryfevx-sfEyba (fake password).

●	Close all windows.

●	Prompt recap (2–3 sentences) In this lab, I was able to crack MD5 passwords very easily utilizing a password cracker. We then experimented with the password cracker to see the strength of passwords and determined a string of randomized, non-repeating letters and numbers are the strongest. 

●	Findings / Steps (bullets or short paragraphs) Our findings concluded that to beat most hash crackers, a good solid randomized, non-repeating set of letters and numbers, I utilize a six-digit-by-three-group pattern with a mass of 20 possible 6-digit letters and numbers such as (fake) xUkhdp which would be assigned a number (15) for example. I could then use groups of three to make passwords. For example, I create a new email and password for a Gmail account. I utilize my password safe and use (14, 7, 2) as my password knowing what each of those numbers represent to create my passwords. Most hash crackers utilize dictionary terms to find matches. That is why a strong password is so important. 

●	Screenshot(s) with redaction, if applicable

 

●	Takeaways (3 bullet points)

○	First, your passwords are not as safe as you might imagine in this day and age with hackers looming at every opportunity to gain access to your information. The best offense is a good defense and should start with a strong password. 

○	Hackers gain access through utilizing your hashes and running them through a hash cracker on the internet with relative ease and looks for patterns of repeating numbers, names, dictionary terms, and cracks them. 

○	The best way to build a (NEARLY) uncrackable password according to Crackstation and my experimentation where you utilize a six digit by three set pattern of randomized, non-repeating upper and lower case letters and numbers.  An example of this would be Dohjvb-w2niax-yvm7sp

●	Privacy: Redact names, emails, IDs, tokens before attaching images.

●	Submit as: .docx or .pdf in that week’s Interactive Activity.



