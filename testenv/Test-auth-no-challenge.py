#!/usr/bin/env python3
from sys import exit
from test.http_test import HTTPTest
from misc.wget_file import WgetFile

"""
    This test ensures Wget's Basic Authorization Negotiation, when the
    --auth-no-challenge command is used.
"""
TEST_NAME = "Auth No Challenge Command"
############# File Definitions ###############################################
File1 = "Need a cookie?"

File1_rules = {
    "Authentication"    : {
        "Type"          : "Basic",
        "User"          : "Pacman",
        "Pass"          : "Omnomnom"
    },
    "ExpectHeader"      : {
        "Authorization" : "Basic UGFjbWFuOk9tbm9tbm9t"
    }
}
A_File = WgetFile ("File1", File1, rules=File1_rules)

WGET_OPTIONS = "--auth-no-challenge --user=Pacman --password=Omnomnom"
WGET_URLS = [["File1"]]

Files = [[A_File]]

ExpectedReturnCode = 0
ExpectedDownloadedFiles = [A_File]

################ Pre and Post Test Hooks #####################################
pre_test = {
    "ServerFiles"       : Files
}
test_options = {
    "WgetCommands"      : WGET_OPTIONS,
    "Urls"              : WGET_URLS
}
post_test = {
    "ExpectedFiles"     : ExpectedDownloadedFiles,
    "ExpectedRetcode"   : ExpectedReturnCode
}

err = HTTPTest (
                name=TEST_NAME,
                pre_hook=pre_test,
                test_params=test_options,
                post_hook=post_test
).begin ()

exit (err)
