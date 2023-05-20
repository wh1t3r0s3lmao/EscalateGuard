#!/usr/bin/env python3
import os
import subprocess

def check_sudoers(target_user):
    sudoers_file = "/etc/sudoers"
    with open(sudoers_file, "r") as f:
        sudoers_content = f.read()

    if target_user in sudoers_content:
        print(f"[!] Potential privilege escalation: {target_user} found in sudoers file.")

def check_sudo_group(target_user):
    command = f"id -nG {target_user} | grep -wq sudo"
    exit_code = os.system(command)

    if exit_code == 0:
        print(f"[!] Potential privilege escalation: {target_user} is a member of the sudo group.")

def check_sudo_version():
    command = "sudo -V | grep -i version"
    output = os.popen(command).read()

    print(f"[*] Sudo version:\n{output}")

def check_kernel_exploits():
    command = "uname -r"
    kernel_version = os.popen(command).read().strip()

    known_exploits = [
        "exploit1",
        "exploit2",
        # Add more known kernel exploits here
    ]

    for exploit in known_exploits:
        if exploit in kernel_version:
            print("[!] Potential privilege escalation: Known kernel exploit present.")

def check_file_permissions(path):
    command = f"stat -c %A {path}"
    permissions = os.popen(command).read().strip()

    if permissions != "600":
        print(f"[!] Potential privilege escalation: Incorrect file permissions for {path}")

def check_abuse_sudo():
    command = "grep -E '^\\s*Defaults\\s+([^#]+,\\s*)?logfile=\\S+\\s*' /etc/sudoers"
    exit_code = os.system(command)

    if exit_code == 0:
        print("[!] Potential privilege escalation: Abuse of sudo (logfile directive).")

def check_setuid_setgid():
    command = "find / -perm -4000 -type f 2>/dev/null"
    setuid_files = os.popen(command).read().splitlines()

    if setuid_files:
        print("[!] Potential privilege escalation: Setuid files present.")

def check_cron_jobs():
    cron_files = [
        "/etc/cron.d/",
        "/etc/cron.daily/",
        "/etc/cron.weekly/",
        "/etc/cron.monthly/",
        "/etc/crontab",
        "/var/spool/cron/"
    ]

    for cron_path in cron_files:
        command = f"ls -la {cron_path} 2>/dev/null"
        output = os.popen(command).read()
        if output:
            print(f"[*] Cron jobs in {cron_path}:\n{output}")

def check_weak_passwords(target_user):
    command = f"sudo -u {target_user} bash -c 'echo checkweakpasswordhere' 2>&1 | grep -q 'checkweakpasswordhere'"
    exit_code = os.system(command)

    if exit_code == 0:
        print("[!] Potential privilege escalation: Weak password.")

def check_suid_guid_files():
    command = "find / -type f \\( -perm -4000 -o -perm -2000 \\) -exec ls -la {} + 2>/dev/null"
    output = os.popen(command).read()

    if output:
        print("[*] SUID/SGID files found:\n{}".format(output))

def check_readable_log_files():
    log_files = [
        "/var/log/auth.log",
        "/var/log/syslog",
        "/var/log/messages",
        # Add more log files to check here
    ]

    for log_file in log_files:
        if os.path.isfile(log_file) and os.access(log_file, os.R_OK):
            print(f"[*] Readable log file found: {log_file}")

def check_service_permissions():
    services = [
        "apache2",
        "nginx",
        "mysql",
        # Add more services to check here
    ]

    for service in services:
        command = f"systemctl show {service}.service --property=Permissions"
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode().strip()
        
        if "=" in output:
            permissions = output.split("=")[1]
            if permissions != "0644":
                print(f"[!] Potential privilege escalation: Incorrect permissions for {service} service")
        else:
            print(f"[!] Unexpected output for {service} service permissions check")

def escalate_privileges():
    target_user = input("Enter the target user: ")

    check_sudoers(target_user)
    check_sudo_group(target_user)
    check_sudo_version()
    check_kernel_exploits()
    check_file_permissions("/etc/passwd")
    check_file_permissions("/etc/shadow")
    check_file_permissions("/etc/sudoers")
    check_abuse_sudo()
    check_setuid_setgid()
    check_cron_jobs()
    check_weak_passwords(target_user)
    check_suid_guid_files()
    check_readable_log_files()
    check_service_permissions()

if __name__ == "__main__":
    escalate_privileges()
