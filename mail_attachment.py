import os
import sys
import win32com.client
import win32com
s= win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
o = win32com.client.Dispatch("Outlook.Application")

    
Msg = o.CreateItem(0)
Msg.To = "recipient@domain.com"
    
Msg.CC = "more email addresses here"
Msg.BCC = "more email addresses here"
    
Msg.Subject = "The subject of you mail"
Msg.Body = "The main body text of you mail"
    
attachment1 = "Path to attachment no. 1"
attachment2 = "Path to attachment no. 2"
Msg.Attachments.Add(attachment1)
Msg.Attachments.Add(attachment2)
 
Msg.Send()