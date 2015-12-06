# Class read list of View Controller defined in file
# then create .h .m file auto
# using for Objective-C
# NhatHM@outlook.com
# 10 days experience in Python

import os
import sys
import datetime
import json
import re


# Function define
def get_list_generated_view_controller(file_list_view_controller):
    print('File listViewController = {}'.format(file_list_view_controller))
    list_class = []
    try:
        file_to_open = open(file_list_view_controller, 'r')
        list_class = file_to_open.read().splitlines()
    except Exception:
        print('*** ERROR *** List your View controllers into file listViewController.txt')
    return list_class


def get_file_content(file_name_get_content):
    return_content = None
    try:
        file_open = open(file_name_get_content, 'r')
        return_content = file_open.read()
    except Exception:
        print("*** ERROR *** Can't open file ", file_name_get_content)
    return return_content


def read_config_file():
    config_content = get_file_content('config_file.json')
    print ('CONFIG_CONTENT = {}'.format(config_content))
    config_dic = json.loads(config_content)
    return config_dic


def get_template_header_h_file(class_name_to_get_template, file_template_header=None):
    # print('File template header = {}'.format(file_template_header))
    if file_template_header is not None:
        default_template_header = get_file_content(file_template_header)
        # Add date time and copy right info into header
        template_class_name = get_name_for_file(class_name_to_get_template)
        template_date_time = datetime.date.today().strftime("%m/%d/%y")
        template_year = datetime.date.today().strftime("%Y")

        # Get list replace value from template file (default_template_header)
        regex = re.compile("__[A-Z]+_[A-Z]+__")
        list_replace_value = re.findall(regex, default_template_header)
        list_value_format = []
        # print(list_replace_value)
        for replace_value in list_replace_value:
            if replace_value == '__CLASS_NAME__':
                value_to_replace = template_class_name
            elif replace_value == '__CREATED_DATE__':
                value_to_replace = template_date_time
            elif replace_value == '__PUBLISH_YEAR__':
                value_to_replace = template_year
            else:
                value_to_replace = config_dictionary[replace_value]

            default_template_header = default_template_header.replace(replace_value, '{}')
            list_value_format.append(value_to_replace)

        # print(list_value_format)
        # print('DEFAULT TEMP HEADER = ')
        # print(default_template_header)
        default_template_header = default_template_header.format(*list_value_format)

        print('====== HEADER =====')
        print(default_template_header)
        return default_template_header
    else:
        # Because of file template header not exist,
        # so we using default template header
        default_template_header = '//\n' \
                                  '//  {0}.h\n' \
                                  '//  {1}\n' \
                                  '//\n' \
                                  '//  Created by {2} on {3}.\n' \
                                  '//  Copyright (c) {4} {5}. All rights reserved.\n' \
                                  '//'
        # Add date time and copy right info into header
        template_class_name = get_name_for_file(class_name_to_get_template)
        template_project_name = 'TemplateProject'
        template_date_time = datetime.date.today().strftime("%m/%d/%y")
        template_year = datetime.date.today().strftime("%Y")
        template_company = 'FPT Software'
        template_customer = 'Apple'
        print(default_template_header)
        default_template_header = default_template_header.format(template_class_name, template_project_name,
                                                                 template_company, template_date_time, template_year,
                                                                 template_customer)
        return default_template_header


def get_template_body_h_file(class_name_to_get_template, file_template_body=None):
    # print('File template body = {}'.format(file_template_body))

    if file_template_body is not None:
        default_template_body = get_file_content(file_template_body)
        template_class_name = get_name_for_file(class_name_to_get_template)
        # Get list replace value from template file (default_template_header)
        regex = re.compile("__[A-Z]+_[A-Z]+__")
        list_replace_value = re.findall(regex, default_template_body)
        list_value_format = []
        # print(list_replace_value)
        for replace_value in list_replace_value:
            if replace_value == '__CLASS_NAME__':
                value_to_replace = template_class_name
            default_template_body = default_template_body.replace(replace_value, '{}')
            list_value_format.append(value_to_replace)

        # print(list_value_format)
        # print('DEFAULT TEMP BODY = ')
        # print(default_template_body)
        default_template_body = default_template_body.format(*list_value_format)
        print('======BODY======')
        print(default_template_body)
        return default_template_body
    else:
        default_template_body = '#import "{0}"\n' \
                                '\n' \
                                '@interface {1} : {2}\n' \
                                '\n' \
                                '@end'

    print(default_template_body)
    return default_template_body.format(base_view_controller + '.h', get_name_for_file(class_name_to_get_template), base_view_controller)


def get_content_h_file(file_name):
    file_h_content = get_template_header_h_file(file_name, h_file_header_template)
    file_h_content = file_h_content + '\n\n' + get_template_body_h_file(file_name, h_file_body_template)
    # print('File H Content = ')
    # print(file_h_content)
    return file_h_content


def export_file_h(file_h_name, file_h_content):
    file_to_save = open(base_folder_to_gen_source + '/' + file_h_name + '.h', 'w')
    file_to_save.write(file_h_content)
    file_to_save.close()


def get_template_header_m_file(class_name_to_get_template, file_template_header=None):
    print('File template header m = {}'.format(file_template_header))
    if file_template_header is not None:
        default_template_header = get_file_content(file_template_header)
        # Add date time and copy right info into header
        template_class_name = get_name_for_file(class_name_to_get_template)
        template_date_time = datetime.date.today().strftime("%m/%d/%y")
        template_year = datetime.date.today().strftime("%Y")

        # Get list replace value from template file (default_template_header)
        regex = re.compile("__[A-Z]+_[A-Z]+__")
        list_replace_value = re.findall(regex, default_template_header)
        list_value_format = []
        # print(list_replace_value)
        for replace_value in list_replace_value:
            if replace_value == '__CLASS_NAME__':
                value_to_replace = template_class_name
            elif replace_value == '__CREATED_DATE__':
                value_to_replace = template_date_time
            elif replace_value == '__PUBLISH_YEAR__':
                value_to_replace = template_year
            else:
                value_to_replace = config_dictionary[replace_value]

            default_template_header = default_template_header.replace(replace_value, '{}')
            list_value_format.append(value_to_replace)

        # print(list_value_format)
        # print('DEFAULT TEMP HEADER = ')
        # print(default_template_header)
        default_template_header = default_template_header.format(*list_value_format)

        print('====== HEADER M =====')
        print(default_template_header)
        return default_template_header
    else:
        # Because of file template header not exist,
        # so we using default template header
        default_template_header = '//\n' \
                                  '//  {0}.m\n' \
                                  '//  {1}\n' \
                                  '//\n' \
                                  '//  Created by {2} on {3}.\n' \
                                  '//  Copyright (c) {4} {5}. All rights reserved.\n' \
                                  '//'

        # Add date time and copy right info into header
        template_class_name = get_name_for_file(class_name_to_get_template)
        template_project_name = 'TemplateProject'
        template_date_time = datetime.date.today().strftime("%m/%d/%y")
        template_year = datetime.date.today().strftime("%Y")
        template_company = 'FPT Software'
        template_customer = 'Apple'
        default_template_header = default_template_header.format(template_class_name, template_project_name, template_company, template_date_time, template_year, template_customer)

        return default_template_header


def get_template_body_m_file(class_name_to_get_template, file_template_body=None):
    print('File template body m = {}'.format(file_template_body))

    if file_template_body is not None:
        default_template_body = get_file_content(file_template_body)
        default_template_body = default_template_body.replace('{', '{{')
        default_template_body = default_template_body.replace('}', '}}')
        template_class_name = get_name_for_file(class_name_to_get_template)
        # Get list replace value from template file (default_template_header)
        regex = re.compile("__[A-Z]+_[A-Z]+__")
        list_replace_value = re.findall(regex, default_template_body)
        list_value_format = []
        print(list_replace_value)
        for replace_value in list_replace_value:
            if replace_value == '__CLASS_NAME__':
                value_to_replace = template_class_name
            default_template_body = default_template_body.replace(replace_value, '{}')
            list_value_format.append(value_to_replace)

        print(list_value_format)
        print('DEFAULT TEMP BODY = ')
        print(default_template_body)
        default_template_body = default_template_body.format(*list_value_format)
        print('======BODY M======')
        print(default_template_body)
        return default_template_body
    else:
        default_template_body = '#import "{0}.h"' \
                                '\n\n' \
                                '@interface {1} ()' \
                                '\n' \
                                '@end' \
                                '\n\n' \
                                '@implementation {2}' \
                                '\n\n' \
                                '- (void)viewDidLoad {3}\n' \
                                '    [super viewDidLoad];\n' \
                                '    // Do any additional setup after loading the view.\n' \
                                '{4}' \
                                '\n\n' \
                                '@end'

        return default_template_body.format(get_name_for_file(class_name_to_get_template),
                                            get_name_for_file(class_name_to_get_template),
                                            get_name_for_file(class_name_to_get_template), '{', '}')


def get_content_m_file(file_name):
    file_m_content = get_template_header_m_file(file_name, m_file_header_template)
    file_m_content = file_m_content + '\n\n' + get_template_body_m_file(file_name, m_file_body_template)
    # print('File M Content = ')
    # print(file_m_content)
    return file_m_content


def export_file_m(file_m_name, file_m_content):
    file_to_save = open(base_folder_to_gen_source + '/' + file_m_name + '.m', 'w')
    file_to_save.write(file_m_content)
    file_to_save.close()


def create_path_for_file(file_name_to_get_path):
    return_path = base_folder_to_gen_source
    path_and_name = file_name_to_get_path.rsplit('/', 1)
    # If len = 1 => only have file name, return base dir
    if len(path_and_name) == 1:
        pass
    # If len = 2 => have sub-dir and file name, return base dir + sub dir
    elif len(path_and_name) == 2:
        return_path = '{0}{1}'.format(return_path, path_and_name[0])

    if not os.path.exists(return_path):
        os.makedirs(return_path)


def get_name_for_file(file_name_to_get_name):
    return_name = file_name_to_get_name
    path_and_name = file_name_to_get_name.rsplit('/', 1)
    # If len = 1 => only have file name, return base dir
    if len(path_and_name) == 1:
        pass
    # If len = 2 => have sub-dir and file name, return base dir + sub dir
    elif len(path_and_name) == 2:
        return_name = path_and_name[1]

    return return_name


# Implement start
# File list View Controller that will be create
file_list_view_controllers = 'listViewController.txt'
base_view_controller = 'BaseViewController'
base_folder_to_gen_source = 'Generated Source'

# Define area, define value that to be replace
defined_class_name = '__CLASS_NAME__'
defined_project_name = '__PROJECT_NAME__'
defined_author_name = '__AUTHOR_NAME__'
defined_created_date = '__CREATED_DATE__'
defined_publish_year = '__PUBLISH_YEAR__'
defined_base_class = '__BASE_CLASS__'


# h file
h_file_header_template = 'h_file_header_template.h'
h_file_body_template = 'h_file_body_template.h'
m_file_header_template = 'm_file_header_template.m'
m_file_body_template = 'm_file_body_template.m'

# Get version to be compare from command line
list_command = sys.argv
config_dictionary = None

if len(list_command) == 1:
    print('List command = {}'.format(list_command))
    config_dictionary = read_config_file()
    print(config_dictionary)
    list_classes = get_list_generated_view_controller(file_list_view_controllers)
    for file_name_to_execute in list_classes:
        create_path_for_file(file_name_to_execute)
        export_file_h(file_name_to_execute, get_content_h_file(file_name_to_execute))
        export_file_m(file_name_to_execute, get_content_m_file(file_name_to_execute))
else:
    print('Arguments invalid')