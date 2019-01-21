# XMedius Cloud User Importer

**This script allows creating XMedius Cloud users from a CSV file.**

In most cases, the XMedius Cloud AD Sync tool is the preferred method to synchronize users between an Active Directory and the XMedius Cloud Portal. However, if customers do not have an Active Directory or simply do not require synchronization beyond the first importation, they still have the option to use a CSV file to import users. This page explains how to do it.

This tool only adds new user account, it does not update existing ones.

# Table of Contents

* [Installation](#installation)
* [Quick Start](#quick-start)
* [File Formats](#file-formats)
* [License](#license)
* [Credits](#credits)

# Installation

## Prerequisites

- Python version 3.7 (minimum) [download](https://www.python.org/downloads/)
- Pip updated to its latest version:
  ```
  pip install --upgrade pip
  ```

## Install Package

From a console, run the following command:

```
$> pip install https://github.com/xmedius/xmc-user-importer/tarball/master
```

# Quick Start

1. Create a configuration file called config.json (replace the values with your own) :

```json
{
  "endpoint": "https://portal.xmedius.com",
  "enterprise_account": "acme",
  "access_token": "1A2B3C...",
  "password_setup_mode": "manual"
}

```

2. Create a csv called sample.csv

```
username,email,last_name,group,password,language
tirion.lanister,tirion.lannister@westeros.com,Lannister,Casterly Rock,P@s$word,en
```

3. Run xmc-user-importer

```
$> xmc-user-importer config.json sample.csv
tirion.lannister@westeros.com... Success
```

# File Formats

## Configuration File Format

The configuration file is a `JSON` file. An example configuration file is provided, see
[config.json](https://github.com/xmedius/xmc-user-importer/blob/master/examples/config.json).

Supported options are:

Option                   | Description
-------------------------|-----------
```endpoint```           | The URL to the XMedius Cloud Portal service ("https://portal.xmedius.com" will be used by default if empty).
```enterprise_account``` | The XMedius Cloud enterprise account.
```access_token```       | The Access Token to be used for authentication with the XMedius Cloud service  It must have the `Manage users` permission.
```password_setup_mode```| Defines how the user's password will be configured (see table below).


```password_setup_mode``` possible values:

Value             | Description
------------------|------------
```manual```      | Reads the password from the CSV file.
```user_choice``` | Does not set a password and lets the portal send the "let the user choose his password" email. Ignores the password value in the CSV file.
```random```      | A random password will be generated for the user, it will not be returned, nor transmitted to the user. Ignores the password value in the CSV file.


## CSV File Format

A sample file is provided, see [sample.csv](https://github.com/xmedius/xmc-user-importer/blob/master/examples/sample.csv). The columns headers must be present.

The comma separated file supports the following column (all values are strings):

Column              | Required | Description
--------------------|----------|-----------
```username```      |        Y | Identifier used to login. Must be unique, may only contain a-z, A-Z, 0-9, hyphen (-), underscore (_) and dot (.).
```email```         |        Y | The email of the user. Must be unique.
```first_name```    |        N | First Name of the user.
```last_name```     |        N | Last Name of the user.
```group```         |        N | Group name to assign the user to. If unspecified or if it does not exist in the enteprise account, the enterprise's default group will be used.
```password```      |      Y/N | Password of user, only required if the `password_setup_mode` is manual, ignored otherwise.
```fax_number```    |        N | Fax number to assign to the user for inbound faxing, in E.164 format.
```salutation```    |        N | Saluation of the user.
```job_title```     |        N | Job Title of the user.
```company_name```  |        N | Company name of the user.
```address```       |        N | Address of the user.
```city```          |        N | City of the user.
```state```         |        N | State of the user.
```country```       |        N | Country of the user.
```zip_code```      |        N | Zip of the user.
```phone_number```  |        N | Phone Number of the user. Can be any string.
```mobile_number``` |        N | Mobile Number of the user. Can be any string.
```language```      |        N | The 2-letter code of user's locale. Supported locales are `EN`, `FR` and `DE`. If unspecified, it will use the enterprise's default language.
```time_zone```     |        N | The name of the user's timezone, allowed values are listed [here](http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html). If unspecified, it will use the enterprise's default time zone.

## Error example

When a user fails to be imported, it will print an error message, with the reason for the failure:

```
$> xmc-user-importer config.json sample-with-invalid-data.csv
email@invalid... Failed: {u'email': [u'does not appear to be valid']}
```


## Note

- It is recommended to test the import on one account first and verify that all flows, including email deliveries, are in line with the expected results
- The script does not write any logs to a file, it only prints messages in the console. So when importing a lot of users, it is a good idea to save the output to a file to find user that failed to be imported
- The password used to create the user will NEVER be sent to newly created user or returned to the
  enterprise administrator running the script. When using `"password_setup_mode": "manual"`, the
  enterprise administrator is responsible to communicate the password to the users.
- The welcome emails and fax number assignation email will follow their relevant enterprise settings.
  - Using `"password_setup_mode": "user_choice"` will always send an email to user requesting him to configure his password.
  - If any email notification is turned on (welcome email, password setup, etc…) provided email addresses must be valid and accepted by your mail server

# License

xmc-user-importer is distributed under [MIT License](https://github.com/xmedius/xmc-user-importer/blob/master/LICENSE).

# Credits

XMedius Cloud User Importer is developed, maintained and supported by
[XMedius Solutions Inc.](https://www.xmedius.com?source=xmc-user-importer)

The names and logos for XMedius Cloud User Importer are trademarks of XMedius Solutions Inc.

![XMedius Logo](https://s3.amazonaws.com/xmc-public/images/xmedius-site-logo.png)

