# EscalateGuard
Introducing EscalateGuard: Your Shield Against Privilege Escalation!

EscalateGuard, a robust Python script, empowers you to fortify your system's defenses against potential privilege escalation vulnerabilities. With its arsenal of automated checks, EscalateGuard acts as your vigilant guardian, tirelessly scanning for security weaknesses and preserving your system's integrity.

Key Features That Make EscalateGuard Shine:

🛡️ Swiftly Unmask Risks: Identify potential privilege escalation threats by pinpointing target users present in the sudoers file, providing invaluable insights.

🔒 Stay One Step Ahead: Detect if a target user is part of the esteemed sudo group, a telltale sign of possible elevated privileges.

🔍 Illuminate the Shadows: Shed light on your system's sudo version, allowing comprehensive analysis and evaluation for any known vulnerabilities.

🚀 Outpace Kernel Exploits: Conduct comprehensive scans for notorious kernel exploits, staying ahead of potential security breaches.

🔐 Fortify File Permissions: Verify the integrity of vital files like /etc/passwd, /etc/shadow, and /etc/sudoers by ensuring correct and secure access restrictions.

🚨 Safeguard Against Misuse: Identify potential abuse of sudo by hunting down the logfile directive, effectively thwarting unauthorized access attempts.

🔑 Lock Down Setuid/Setgid Files: Spot files with setuid/setgid permissions that may serve as gateways for unauthorized privilege escalation.

📜 Monitor Log Files: Keep a watchful eye on readable log files, safeguarding sensitive information and maintaining system transparency.

🔒 Restrict Service Access: Validate service permissions, ensuring correct and secure access rights for services like Apache, Nginx, and MySQL.

⚡ Streamlined Experience: Enjoy the benefits of an intuitive command-line interface, enabling quick and efficient security assessments.
   
   ---How to use---
   To use the script:
   git clone https://github.com/wh1t3r0s3lmao/EscalateGuard
   cd EscalateGuard
   python EscalateGuard.py
   
   
   
   Enjoy <3
~P.S, It's just an alpha version of my script! If there's any issues or bugs i'd like to hear it from you!
