#!/usr/bin/env python
# 
# Author: Jose Lo Huang
# Creation Date: 28/11/2020
# Updates:
# 03/12/2020 - Add comments and minor fixes
# 
# This program will be in charge of the following main tasks:
# 1. Request the number of EC2 instances to create
# 2. Create the Ansible playbook that will create the EC2 instances
# 3. Run the Ansible playbook that will create the EC2 instances
# 4. Create the Ansible playbook that will install Apache2 on the new EC2 instances
# 5. Run the Ansible playbook that will install Apache2 on the new EC2 instances
# 

import boto
import os


def general_error(error):
    #
    # This function is to print a general error message if there is an unexpected error
    # 
    print()
    print("******************************************************************")
    print(str(error)+". Check the following: ")
    print("1. Your internet connection ")
    print("2. Your AWS permissions ")
    print("3. Your AWS access key ID and Secret Access Key ID ")
    print("******************************************************************")
    print()


def write_create_playbook(value):
    #
    # This procedure creates the Ansible playbook that will create the EC2 instances.
    # 
    try:
        print("**************************************************************")
        print("****************** CREATING LAUNCH PLAYBOOK ******************")
        print("**************************************************************")
        output_file = open('instance_launcher.yml','w')
        line2 = "- name: Ansible"
        line3 = " hosts: localhost"
        line4 = " tasks:"
        line5 = " - name: launching AWS instances using Ansible"
        line6 = "    ec2:"
        line7 = "    instance_type: t2.micro"
        line8 = "    image: ami-0dc8d444ee2a42d8a"
        line9 = "    region: eu-west-1"
        line10 = "    wait: yes"
        line11 = "     count: "+value
        line12 = "    vpc_subnet_id: subnet-b0f9fed6"
        line13 = "    assign_public_ip: yes"
        line14 = "    aws_access_key: AKIA****************"
        line15 = "    aws_secret_key: ****************************************"
        line18 = "     group_id: sg-0e19ba529c4f5a36f"
        line19 = "    key_name: CIT-DUB"
        line16 = "    instance_tags: "
        line17 = "      Name: Webserver"
        output_file.write("%s \n %s \n %s \n %s \n" % (line2, line3, line4, line5))
        output_file.write("%s \n %s \n %s \n %s \n %s \n" % (line6, line7, line8, line9, line10))
        output_file.write("%s \n %s \n %s \n %s \n %s \n" % (line11, line12, line13, line14, line15))
        output_file.write("%s \n %s \n %s \n %s \n" % (line18, line19, line16, line17))
        output_file.close()
        os.system('cat instance_launcher.yml')
    except:
        general_error("There was an error while writing the instance_launcher.yml file")


def run_create_playbook():
    #
    # This procedure runs the Ansible playbook that will create the EC2 instances.
    # 
    try:
        print("**************************************************************")
        print("******************** LAUNCHING INSTANCES *********************")
        print("**************************************************************")
        os.system('ansible-playbook instance_launcher.yml')
    except:
        general_error("There was an error while running the instance_launcher.yml file")


def refresh_cache():
    #
    # This method is in charge of refreshing the dynamic hosts inventory
    #
    try:
        print("**************************************************************")
        print("**************** REFRESHING ANSIBLE INVENTORY ****************")
        print("**************************************************************")
        os.system('ec2.py --list --refresh-cache')
    except:
        general_error("There was an error while refreshing the Ansible cache.")


def write_install_playbook():
    #
    # This procedure creates the Ansible playbook that will install Apache2.
    # 
    try:
        print("**************************************************************")
        print("****************** CREATING INSTALL PLAYBOOK *****************")
        print("**************************************************************")
        output_file = open('instance_installer.yml','w')
        line2 = "- name: Install Apache"
        line3 = " hosts: all"
        line10 = " become: yes"
        line4 = " tasks:"
        line5 = " - name: installing Apache on AWS instances using Ansible"
        line6 = "    apt:"
        line7 = "    name: apache2"
        line8 = "    state: present"
        line9 = "    update_cache: yes"
        line11 = "  - name: start Apache "
        line12 = "   service:"
        line13 = "     name: apache2"
        line14 = "     state: started"
        output_file.write("%s \n %s \n %s \n %s \n %s \n" % (line2, line3, line10, line4, line5))
        output_file.write("%s \n %s \n %s \n %s \n" % (line6, line7, line8, line9))
        output_file.write("%s \n %s \n %s \n %s \n" % (line11, line12, line13, line14))
        output_file.close()
        os.system('cat instance_installer.yml')
    except:
        general_error("There was an error while creating the instance_installer.yml file.")


def run_install_playbook():
    #
    # This procedure runs the Ansible playbook that install Apache2.
    # 
    try:
        print("**************************************************************")
        print("*************** INSTALLING APACHE ON THE FLEET ***************")
        print("**************************************************************")
        os.system('ansible-playbook -i /etc/ansible/ec2.py --limit "tag_Name_Webserver" --private-key=CIT-DUB.pem instance_installer.yml')
    except:
        general_error("There was an error while running the instance_launcher.yml file")


def main():
    #
    # MAIN PROGRAM
    #
    print("==================================================================")
    print("AWS Ansible Playbook v1.0 powered by CIT, AWS, Python2 and Ansible")
    print("Author: Jose Lo Huang. All rights reserved using the MIT License. ")
    print("Complete instructions on the README.txt file. Hit 'ENTER' to exit.")
    print("==================================================================")
    while True:
        correct_credentials = ['AKIA****************','****************************************']
        # Request the number of instances to create
        print("Please insert the number of EC2 instances to create. ")
        value = str(raw_input("Possible values are 1, 2, 3, 4 and 5. Or 'Enter' to exit: "))
        # If user hit 'Enter', the program finishes.
        if (value == None) or (value == ""):
            print("******************************************************************")
            print("Exiting.")
            return
        # If user enter word with lenght >1
        if (len(value) != 1):
            print("******************************************************************")
            print("The value "+value+" is not a valid option.")
            continue
        # Check that user entered a value between 1 and 5
        if (49 <= ord(value) <= 53):
            # Create the instance_launcher.yml file
            write_create_playbook(value)
            # Run the instance_launcher.yml file
            run_create_playbook()
            # Refresh the Ansible dynamic hosts cache
            refresh_cache()
            # Create the instance_installer.yml file
            write_install_playbook()
            # Run the instance_installer.yml file
            run_install_playbook()
        else:
            print("******************************************************************")
            print("The value "+value+" is not a valid option.")


#
# PROGRAM RUN
# 
main()


