
#! /usr/bin/python

#___________________________________________________________________________________________________________________________________________
#							Importing Necessary Libraries
#___________________________________________________________________________________________________________________________________________

from Tkinter import *
try:
  import Tkinter              # Python 2
  import ttk
  import tkMessageBox
except ImportError:
  import tkinter as Tkinter   # Python 3
  import tkinter.ttk as ttk
import time
import datetime
import pandas as pd
from pandas import Series as s
from pandas import DataFrame as df
import os
from pyspark import SparkContext
from pyspark.sql.types import *
from pyspark.sql import SQLContext
from pyspark.sql import *

logFile = "/usr/local/spark/README.md"  # Should be some file on your system
sc = SparkContext("local", "Simple App")
sqlContext = SQLContext(sc)
logData = sc.textFile(logFile).cache()
pd.set_option('display.height', 500)
pd.set_option('display.max_rows', 1000000)

#_________________________________________________________________________________________________________________________________________
#							Defining the Variables
#_________________________________________________________________________________________________________________________________________
mwin=Tk()
os.chdir(os.getcwd()) # Current Directory to save our exported Files
time1=''
filename1 = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
text_input1=StringVar()
text_input2=StringVar()
text_input3=StringVar()
text_input4=StringVar()
opera=StringVar()
opera1=StringVar()
var=int
fname=str('Counterwise_Report_'+filename1+'.csv')
fname1=str('Datewise_Report_'+filename1+'.csv')
sdate='None'
edate='None'
d=df()
l=StringVar()
x='None'
x1='None'
r=5
j=5
k=0.0
temp2=5


#____________________________________________________________________________________________________________________________________________#
#							Frame Configuration
#___________________________________________________________________________________________________________________________________________

mwin.geometry('1600x800')
mwin.title("Devswom Annual Reporting Tool")

tops=Frame(mwin,width=1600,height=50,relief=SUNKEN)
tops.pack(side=TOP)

f1=Frame(mwin,width=400,height=750)
f1.pack(side=LEFT)

f2=Frame(mwin,width=400,height=550)
f2.pack(side=TOP)

#top = Toplevel()

#________________________________________________________________________________________________________________________________________
#								Defining the Functions
#_________________________________________________________________________________________________________________________________________

def tick():
 global time1
 time2=datetime.datetime.now().strftime('%d-%b-%Y   %H:%M:%S')
 if time2 !=time1:
  time1=time2
  tlabel.config(text=time2)
 tlabel.after(20,tick) 

def read_csv():
 global d
 global filename1
 global fname
 global x
 global x1
 global l
 global k
 global lst2
 if(sdate=='DD-MM-YYYY'):
  if(x!="'None'"):
   lst2=list(d.columns)
   fname=str('Counter_'+x+'_'+filename1+'.csv')
 elif(x==''):
  if(sdate!='DD-MM-YYYY' and edate!='DD-MM-YYYY'):
   lst2=list(d.columns)
   fname=str('Datewise_Report-'+filename1+'.csv')
 else:
   lst2=list(d.columns)
   fname=str('Datewise_Report for Counter '+x+'_'+filename1+'.csv')
 id1=len(d.index)
 lst=list(['','Total',k])
 dataframe=df([lst],index=[id1+1],columns=lst2)
 temp=d.append(dataframe)
 temp.to_csv(fname,mode='a',index=FALSE)


def exit(*args):
 quit()


def rbut1():
 global x
 global x1
 x=str(opera.get())
 x1=str(opera1.get())
 global sdate
 sdate=str(text_input1.get())
 global edate
 global d
 global filename1
 global fname
 edate=str(text_input2.get())
 if(date_length()==False):
  if(tkMessageBox.askyesno("Action Required !!!",""" You are about to Generate the Report ...
This might takes several minutes depending on your System Performance
Are you Sure you want to Continue ???""")==True):
   view()
   if(x==''):
    if(text_input.get()!='DD-MM-YYYY' and text_input1.get()!='DD-MM-YYYY'):
     sdate=datetime.datetime.strptime(text_input.get(), "%d-%m-%Y").strftime("%Y-%m-%d")
     edate=datetime.datetime.strptime(text_input1.get(), "%d-%m-%Y").strftime("%Y-%m-%d")
     droptable()
     fdate()
     onlydate()
     droptable()
     clear()
    if(tkMessageBox.askyesno("Action Required !!!"," Click Yes to Save the Report")==True):
	read_csv()
   else:
    sdate=datetime.datetime.strptime(text_input.get(), "%d-%m-%Y").strftime("%Y-%m-%d")
    edate=datetime.datetime.strptime(text_input1.get(), "%d-%m-%Y").strftime("%Y-%m-%d")
    droptable()
    counter()
    counterwithdate()
    droptable()
#    top.after(1, top.destroy)
    clear()
    if(tkMessageBox.askyesno("Action Required !!!"," Click Yes to Save the Report")==True):
	read_csv()
  else:
   tkMessageBox.showinfo("Oops !!!","Please select your Option Again") 
   clear()
 elif(text_input.get()=='DD-MM-YYYY'):
    if(x!="'None'"):
     if(tkMessageBox.askyesno("Action Required !!!",""" You are about to Generate the Report ...
This might takes several minutes depending on your System Performance
Are you Sure you want to Continue ???""")==True):
      view()
      droptable()
      counter()
      onlycounter()
      droptable()
#      top.after(1, top.destroy)
      clear()
      if(tkMessageBox.askyesno("Action Required !!!"," Click Yes to Save the Report")==True):
	read_csv()
     else:
      tkMessageBox.showinfo("Oops !!!","Please select your Option Again") 
      clear()

def rbut2():
 global x
 global x1
 x=opera.get()
 x1=opera1.get()
 global sdate
 sdate=str(text_input1.get())
 global edate
 global d
 global filename1
 global fname
 edate=str(text_input2.get())
 testdate=str(datetime.datetime.now().strftime('%Y-%b-%d'))
 if(date_length()==False):
  if(tkMessageBox.askyesno("Action Required !!!",""" You are about to Generate the Report ...
This might takes several minutes depending on your System Performance
Are you Sure you want to Continue ???""")==True):
   view()
   if(x==''):
    if(edate!='DD-MM-YYYY' and sdate!='DD-MM-YYYY'):
     sdate=datetime.datetime.strptime(sdate, "%d-%m-%Y").strftime("%Y-%m-%d")
     edate=datetime.datetime.strptime(edate, "%d-%m-%Y").strftime("%Y-%m-%d")
     droptable()
     fdate()
     onlydate()
     droptable()
     clear()
     if(tkMessageBox.askyesno("Action Required !!!"," Click Yes to Save the Report")==True):
	read_csv()
   else:
    sdate=datetime.datetime.strptime(sdate, "%d-%m-%Y").strftime("%Y-%m-%d")
    edate=datetime.datetime.strptime(edate, "%d-%m-%Y").strftime("%Y-%m-%d")
    droptable()
    counter()
    counterwithdate()
    droptable()
#    top.after(1, top.destroy)
    clear()
    if(tkMessageBox.askyesno("Action Required !!!"," Click Yes to Save the Report")==True):
	read_csv()
  else:
   tkMessageBox.showinfo("Oops !!!","Please select your Option Again")
   clear() 
 elif(sdate=='DD-MM-YYYY'):
    if(x!="'None'"):
     if(tkMessageBox.askyesno("Action Required !!!",""" You are about to Generate the Report ...
This might takes several minutes depending on your System Performance
Are you Sure you want to Continue ???""")==True):
      view()
      droptable()
      counter()
      onlycounter()
      droptable()
#      top.after(1, top.destroy)
      clear()
      if(tkMessageBox.askyesno("Action Required !!!"," Click Yes to Save the Report")==True):
	read_csv()
     else:
      tkMessageBox.showinfo("Oops !!!","Please select your Option Again") 
      clear()
 

def rbut_popup():
 global x
 global x1
 x=opera.get()
 x1=opera1.get()
 global sdate
 sdate=str(text_input3.get())
 edate=str(text_input4.get())
 global edate
 global d
 global filename1
 global fname
 if(date_length()==False):
  sdate=datetime.datetime.strptime(sdate, "%d-%m-%Y").strftime("%Y-%m-%d")
  edate=datetime.datetime.strptime(edate, "%d-%m-%Y").strftime("%Y-%m-%d")
  if (opera1.get()=="''"):
   popup()
   opera1.set("''")
  elif(opera1.get()=="''" and  textbox3.get()!='DD-MM-YYYY'):
   popup()
   opera1.set("''")
  else:
   if(tkMessageBox.askyesno("Action Required !!!",""" You are about to Generate the Report ...
This might takes several minutes depending on your System Performance
Are you Sure you want to Continue ???""")==True):
    view()
    droptable()
    counter()
    counterwithdate()
    droptable()
    clear()
    if(tkMessageBox.askyesno("Action Required !!!"," Click Yes to Save the Report")==True):
  	read_csv()
   else:
     tkMessageBox.showinfo("Oops !!!","Please select your Option Again")
     clear()

def mandatory():
	if(text_input1.get()!='YYYY-MM-DD' and opera1.get()==''):
		popup()
		text_input1.focus_set()
		text_input2.focus_set()


def clear():
 opera.set("''")
 opera1.set("''")
 if (textbox.get()!='DD-MM-YYYY' and textbox1.get()!='DD-MM-YYYY'):
  textbox.delete('0',END)
  textbox.config(fg='grey')
  textbox.insert(0,'DD-MM-YYYY')
  textbox1.delete("0",END)
  textbox1.config(fg='grey')
  textbox1.insert(END,'DD-MM-YYYY')
 elif (textbox2.get()!='DD-MM-YYYY' and textbox3.get()!='DD-MM-YYYY'):
  textbox2.delete("0",END)
  textbox2.config(fg='grey')
  textbox2.insert(END,'DD-MM-YYYY')
  textbox3.delete("0",END)
  textbox3.config(fg='grey')
  textbox3.insert(END,'DD-MM-YYYY')

def on_entry(event):
 if (textbox.get()=='DD-MM-YYYY'):
  textbox.delete('0',END)
  textbox.config(fg='black')
  textbox.insert(0,"")


def on_entry1(event):
 if (textbox1.get()=='DD-MM-YYYY'):
  textbox1.delete('0',END)
  textbox1.config(fg='black')
  textbox1.insert(0,"")


def on_entry2(event):
 if(textbox2.get()=='DD-MM-YYYY'):
  textbox2.delete('0',END)
  textbox2.config(fg='black')
  textbox2.insert(0,"")

def on_entry3(event):
 if(textbox3.get()=='DD-MM-YYYY'):
  textbox3.delete('0',END)
  textbox3.config(fg='black')
  textbox3.insert(0,"")

def focus_out(event):
 if(textbox.get()==''):
  textbox.insert(0,'DD-MM-YYYY')
  textbox.config(fg='grey')


def focus_out1(event):
 if(textbox1.get()==''):
  textbox1.insert(0,'DD-MM-YYYY')
  textbox1.config(fg='grey')

def focus_out2(event):
 if(textbox2.get()==''):
  textbox2.insert(0,'DD-MM-YYYY')
  textbox2.config(fg='grey')

def focus_out3(event):
 if(textbox3.get()==''):
  textbox3.insert(0,'DD-MM-YYYY')
  textbox3.config(fg='grey')



def view():
 global d
 global op
 global sdate
 global edate
 global fname
 global filename1


 bmvazhipadumaster= sqlContext.read.format("jdbc").option("url", "jdbc:mysql://localhost/bookingmaster?useSSL=false").option("driver", "com.mysql.jdbc.Driver").option("dbtable", "bmvazhipadumaster").option("user", "username").option("password", "password").load()

 cbdetailtrans= sqlContext.read.format("jdbc").option("url", "jdbc:mysql://localhost/currentbooking?useSSL=false").option("driver", "com.mysql.jdbc.Driver").option("dbtable", "cbdetailtrans").option("user", "username").option("password", "password").load()

 cbbooktrans= sqlContext.read.format("jdbc").option("url", "jdbc:mysql://localhost/currentbooking?useSSL=false").option("driver", "com.mysql.jdbc.Driver").option("dbtable", "cbbooktrans").option("user", "username").option("password", "password").load()

 abreceipttransaction= sqlContext.read.format("jdbc").option("url", "jdbc:mysql://localhost/advancebooking?useSSL=false").option("driver", "com.mysql.jdbc.Driver").option("dbtable", "abreceipttransaction").option("user", "username").option("password", "password").load()

 abvazhtransaction= sqlContext.read.format("jdbc").option("url", "jdbc:mysql://localhost/advancebooking?useSSL=false").option("driver", "com.mysql.jdbc.Driver").option("dbtable", "abvazhtransaction").option("user", "username").option("password", "password").load()

 abvazhtransaction.registerTempTable("abvazhtransaction")
 abreceipttransaction.registerTempTable("abreceipttransaction")
 cbdetailtrans.registerTempTable("cbdetailtrans")
 cbbooktrans.registerTempTable("cbbooktrans")
 bmvazhipadumaster.registerTempTable("bmvazhipadumaster")

def fdate():
	global d
	global l
	global sdate
	global edate
	global fname
	global fname1
	global x
	global x1
	if(x==''):
		x=x1
	date_filter=sqlContext.sql("create temporary view fdate as select cmachineid as Counter_Name,vazhname as Vazhipadu_Name,sum(total) as Collection from (select cmachineid,vazhname,total from (select l.cmachineid,k.vazhname,l.total from bmvazhipadumaster k join (select i.cmachineid,j.vazhid,sum(j.vamount) as total from bmcountermaster i join (select g.counterid,h.vazhid,h.vamount from abreceipttransaction g join abvazhtransaction h on g.TransYear=h.TransYear and g.TransNo=h.TransNo where date(g.tdate)>='%s' and date(g.tdate)<='%s') j on i.counterid=j.counterid  group by i.cmachineid,j.vazhid) l on k.vazhid=l.vazhid group by l.cmachineid,k.vazhname,l.total order by l.cmachineid) m union all select cmachineid,vazhname,total from (select e.cmachineid,f.vazhname,e.total from (select c.cmachineid,d.vazhid,sum(d.vvalue) as total from bmcountermaster c join (select a.vazhid,a.transno,a.vvalue,b.transcounter,b.transdate from cbdetailtrans a join cbbooktrans b on a.transno=b.transno and b.transdate>='%s' and b.transdate<='%s') d on c.counterid=d.transcounter group by c.cmachineid,d.vazhid) e join bmvazhipadumaster f on e.vazhid=f.vazhid group by e.cmachineid,f.vazhname,e.total) n) o group by cmachineid,vazhname order by cmachineid,vazhname"%(sdate,edate,sdate,edate)).toPandas()


def counter():
	global d
	global l
	global sdate
	global edate
	global fname
	global fname1
	global x
	global x1
	if(x==''):
		x=x1
	counter_filter=sqlContext.sql("create temporary view counter as select tdate as Transaction_Date,vazhname as Vazhipadu_Name,sum(total) as Collection from (select date(tdate),vazhname,total from (select l.tdate,k.vazhname,l.total from bmvazhipadumaster k join (select j.tdate,j.vazhid,sum(j.vamount) as total from bmcountermaster i join (select g.tdate,g.counterid,h.vazhid,h.vamount from abreceipttransaction g join abvazhtransaction h on g.TransYear=h.TransYear and g.TransNo=h.TransNo) j on i.counterid=j.counterid where i.cmachineid=%s group by j.tdate,j.vazhid) l on k.vazhid=l.vazhid group by l.tdate,k.vazhname,l.total order by l.tdate) m union all select transdate,vazhname,total from (select e.transdate,f.vazhname,e.total from (select d.transdate,d.vazhid,sum(d.vvalue) as total from bmcountermaster c join (select a.vazhid,a.transno,a.vvalue,b.transcounter,b.transdate from cbdetailtrans a join cbbooktrans b on a.transno=b.transno) d on c.counterid=d.transcounter where c.cmachineid=%s group by d.transdate,d.vazhid) e join bmvazhipadumaster f on e.vazhid=f.vazhid group by e.transdate,f.vazhname,e.total) n) m group by tdate,vazhname order by tdate,vazhname"%(x,x)).toPandas()


def droptable():
	sqlContext.sql("drop table if exists fdate")
	sqlContext.sql("drop table if exists counter")


#to view/save overall counter report from counter table with only Date
def onlydate():
	global d
	global l
	global sdate
	global k
	global edate
	global fname
	global filename1
	d=sqlContext.sql("SELECT * FROM fdate").toPandas()
	total=sqlContext.sql("select sum(collection) as total from fdate").toPandas()
	k=total['total'][0]
	l="\n\n Total  Collection for the period of %s to %s is\t%f"%(sdate,edate,k)
	tbox1.delete('1.0',END)
	tbox1.insert(CURRENT,d)
	tbox2.delete('1.0',END)
	tbox2.insert(END,l)
 
#to view/save overall counter report from counter table with only Counter Name
def onlycounter():
	global d
	global op
	global sdate
	global edate
	global fname
	global k
	global x
	global filename1
	d=sqlContext.sql("select * from counter").toPandas()
	total=sqlContext.sql("select sum(collection) as total from counter").toPandas()
	k=total['total'][0]
	l="\n\n Total Collection for Counter %s is \t%f"%(x,k)
	tbox1.delete('1.0',END)
	tbox1.insert(CURRENT,d)
	tbox2.delete('1.0',END)
	tbox2.insert(END,l)

# to get the report based on machineid and date
def datewithcounter():
	global d
	global op
	global sdate
	global edate
	global fname
	global x
	global filename1
	global k
	d=sqlContext.sql("SELECT * FROM fdate where cmachineid=%s"%x).toPandas()
	total=sqlContext.sql("select sum(collection) as total from fdate").toPandas()
	k=total['total'][0]
	l="\n\n Total Collection for Counter %s for a Period of %s to %s is\t%f"%(x,sdate,edatek)
	tbox1.delete('1.0',END)
	tbox1.insert(CURRENT,d)
	tbox2.delete('1.0',END)
	tbox2.insert(END,l)

#if date and counter both are given (for either table it will work)
def counterwithdate():
	global d
	global op
	global k
	global sdate
	global x
	global x1
	global edate
	global fname
	global fname1
	d=sqlContext.sql("select * from counter where Transaction_Date>='%s' and Transaction_Date<='%s'"%(sdate,edate)).toPandas()
	total=sqlContext.sql("select sum(collection) as total from counter where Transaction_Date>='%s' and Transaction_Date<='%s'"%(sdate,edate)).toPandas()
	k=total['total'][0]
	l="\n\nTotal Collection for Counter %s for period of %s to %s is\t %f"%(x1,sdate,edate,k)
	tbox1.delete('1.0',END)
	tbox1.insert(CURRENT,d)
	tbox2.delete('1.0',END)
	tbox2.insert(END,l)
 
def bmcountermaster():
 bmcountermaster= sqlContext.read.format("jdbc").option("url", "jdbc:mysql://localhost/bookingmaster?useSSL=false").option("driver", "com.mysql.jdbc.Driver").option("dbtable", "bmcountermaster").option("user", "root").option("password", "redhat").load()
 bmcountermaster.registerTempTable("bmcountermaster")

	
def date_length():
	page1_sdate=textbox.get()
	page1_edate=textbox1.get()
	page2_sdate=textbox2.get()
	page2_edate=textbox3.get()
	if(page1_sdate!='DD-MM-YYYY' and page1_edate!='DD-MM-YYYY'):
		if(len(page1_edate)>10 or len(page1_edate)<10):
			tkMessageBox.showerror("Error","Incorrect Length for End Date")
			return True
		elif(len(page1_sdate)>10 or len(page1_sdate)<10):
			tkMessageBox.showerror("Error","Incorrect Length for Start Date")
			return True
		elif(page1_sdate.index('-')!=2 and page1_sdate.index('-')!=5):
			tkMessageBox.showerror("Error","Incorrect Date Delimiter at Start Date")
			return True
		elif(page1_edate.index('-')!=2 and page1_edate.index('-')!=5):
			tkMessageBox.showerror("Error","Incorrect Date Delimiter at End Date")
			return True
		elif(int(page1_edate[3:5])>12 or int(page1_edate[0:2])>31):
			tkMessageBox.showerror("Error","Wrong Value for Date/Month in End Date")
			return True
		elif(int(page1_sdate[3:5])>12 or int(page1_sdate[0:2])>31):
			tkMessageBox.showerror("Error","Wrong Value for Date/Month in Start Date")
			return True
		elif(int(page1_sdate[3:4])>=2 or int(page1_sdate[0:1])>3):
			tkMessageBox.showerror("Error","Wrong Value for Date/Month in Start Date")
			return True
		elif(int(page1_edate[3:4])>=2 or int(page1_edate[0:1])>3):
			tkMessageBox.showerror("Error","Wrong Value for Date/Month in End Date")
			return True
		elif(int(page1_sdate[6:])>int(page1_edate[6:])):
			tkMessageBox.showerror("Error","Wrong Value for Year in Start Date")
			return True
		else:
			return False
	elif(page2_sdate!='DD-MM-YYYY' and page2_edate!='DD-MM-YYYY'):
		if(len(page2_sdate)>10 or len(page2_sdate)<10):
			tkMessageBox.showerror("Error","Incorrect Length for Start Date")	
			return True
		elif(len(page2_edate)>10 or len(page2_edate)<10):
			tkMessageBox.showerror("Error","Incorrect Length for End Date")	
			return True
		elif(page2_sdate.index('-')!=2 and page2_sdate.index('-')!=5):
			tkMessageBox.showerror("Error","Incorrect Date Delimiter at Start Date")	
			return True
		elif(page2_edate.index('-')!=2 and page2_edate.index('-')!=5):
			tkMessageBox.showerror("Error","Incorrect Date Delimiter at End Date")	
			return True
		elif(int(page2_edate[3:5])>12 or int(page2_edate[0:2])>31):
			tkMessageBox.showerror("Error","Wrong Value for Date/Month in End Date")
			return True
		elif(int(page2_sdate[3:5])>12 or int(page2_sdate[0:2])>31):
			tkMessageBox.showerror("Error","Wrong Value for Date/Month in Start Date")
			return True
		elif(int(page2_sdate[3:4])>=2 or int(page2_sdate[0:1])>3):
			tkMessageBox.showerror("Error","Wrong Value for Date/Month in Start Date")
			return True
		elif(int(page2_edate[3:4])>=2 or int(page2_edate[0:1])>3):
			tkMessageBox.showerror("Error","Wrong Value for Date/Month in End Date")
			return True
		elif(int(page2_sdate[6:])>int(page2_edate[6:])):
			tkMessageBox.showerror("Error","Wrong Value for Year in Start Date")
			return True
		else:
			return False

def popup():
	tkMessageBox.showerror("Error!!!!","Both Date (YYYY-MM-DD) and Counter Fields are Mandatory")
	opera1.set("''")




#def progress():
#	top.title("Please Wait !!!!")
#	tkMessageBox.showinfo("Please Wait","Generating Report .....")
#	Message(top, text=" Generating the Report ... ", width=50).pack()
#	progressbar=ttk.Progressbar(top,orient=HORIZONTAL,length=200).pack()
#	progressbar.config(mode='indeterminate')
#	progressbar.start()
#	top.after(timer, top.destroy)	

#_________________________________________________________________________________________________________________________________________
#							Framing the Buttons/Labels/Textbox
#_________________________________________________________________________________________________________________________________________
bmcountermaster()
count=sqlContext.sql("select DISTINCT(cmachineid) from bmcountermaster order by cmachineid ASC").toPandas();
counters=count.transpose()
counters1=counters.values

#Labels
lb=Label(tops,font=('calibri',36,'bold'),text="Devaswom Temple Annual Reporting Tool",fg='orange',bg="powder blue")
lb.grid(row=0,column=0,sticky=N,columnspan=100,padx=100)


tlabel=Label(f2,font=('calibri',15,'bold'),bg='light green')
tlabel.grid(row=1,column=0,sticky=N,padx=100,pady=10)
tick()


lb2=Label(f2,text='\n\n')
lb2.grid(row=3,column=0)

n=ttk.Notebook(f2)
n.grid(row=3,column=0,sticky=N)
page1=Frame(n)
page2=Frame(n)
page3=Frame(n)


#Radio Buttons

n.add(page1,text="Datewise Data")
n.add(page2,text="Counter wise Data")
n.add(page3,text="Counter and Date wise")

lb11=Label(page1,font=('calibri',12,'bold'),text='\n\nPlease Select Start and End Date\t\t\n')
lb11.grid(row=4,column=0,sticky=W)
lb1=Label(page1,font=('calibri',10,'bold'),text='Start Date :-\t\t')
lb1.grid(row=21,column=0,sticky=W,padx=100)
lb3=Label(page1,font=('calibri',10,'bold'),text='End Date :-\t\t')
lb3.grid(row=23,column=0,sticky=W,padx=100)
page1_lb2=Label(page1,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
page1_lb2.grid(row=24,column=0)

lb1=Label(page2,font=('calibri',12,'bold'),text='\n\nPlease Select the Required Counter\t\t')
lb1.grid(row=4,column=0,sticky=E)


for tp in counters1[0]:
	text1="For Counter "+ str(tp)
	if(str(tp)!='None'):	
		Radiobutton(page2,text=text1,variable=opera,value=str("'"+tp+"'")).grid(row=j,column=0,sticky=W)
	r=r+1
	j=j+1

page1_but1=Button(page1, text="Export to CSV",command=read_csv)
page1_but=Button(page1,text="View",command=rbut1)
page1_but.grid(row=25,column=0,sticky=W)
page1_but1.grid(row=25,column=0,columnspan=200,padx=50,pady=5,sticky=N)
page1_but5=Button(page1,text="   Exit   ",command=exit)
page1_but5.grid(row=25,column=0,sticky=E,columnspan=200)


page2_lb2=Label(page2,text='\n\n')
page2_lb2.grid(row=24,column=0)
page2_but1=Button(page2, text="Export to CSV",command=read_csv)
page2_but=Button(page2,text="View",command=rbut2)
page2_but.grid(row=25,column=0,sticky=W)
page2_but1.grid(row=25,column=0,columnspan=200,padx=50,pady=5,sticky=N)
page2_but5=Button(page2,text="   Exit   ",command=exit)
page2_but5.grid(row=25,column=0,sticky=E,padx=50)


page3_but1=Button(page3, text="Export to CSV",command=read_csv)
page3_but=Button(page3,text="View",command=rbut_popup)
page3_but.grid(row=25,column=0,sticky=W)
page3_but1.grid(row=25,column=0,columnspan=200,padx=50,pady=5,sticky=N)
page3_but5=Button(page3,text="   Exit   ",command=exit)
page3_but5.grid(row=25,column=0,sticky=E,padx=50)




lb1=Label(page3,font=('calibri',12,'bold'),text='\n\nPlease Select the Required Counter and Date\t\t\t')
lb1.grid(row=4,column=0,sticky=E)
lb1=Label(page3,font=('calibri',10,'bold'),text='Start Date :-\t\t')
lb1.grid(row=21,column=0,sticky=W,padx=200)
lb3=Label(page3,font=('calibri',10,'bold'),text='End Date :-\t\t')
lb3.grid(row=23,column=0,sticky=W,padx=200)

for i in counters1[0]:
	text1="For Counter "+ str(i)
	if(str(i)!='None'):	
		Radiobutton(page3,text=text1,variable=opera1,value=str("'"+i+"'")).grid(row=temp2,column=0,sticky=W)
	r=r+1
	temp2=temp2+1


#TextBox and Entry

textbox=Entry(page1,textvariable=text_input1,font=('bold',10))
textbox.insert(END,'DD-MM-YYYY')
textbox.config(fg='grey')
textbox.bind('<FocusIn>',on_entry)
textbox.bind('<FocusOut>',focus_out)
textbox.grid(row=21,column=0,columnspan=1,sticky=E,padx=50)

textbox1=Entry(page1,textvariable=text_input2,font=('bold',10))
textbox1.insert(END,'DD-MM-YYYY')
textbox1.config(fg='grey')
textbox1.bind('<FocusIn>',on_entry1)
textbox1.bind('<FocusOut>',focus_out1)
textbox1.grid(row=23,column=0,columnspan=1,sticky=E,padx=50)


textbox2=Entry(page3,textvariable=text_input3,font=('bold',10))
textbox2.insert(END,'DD-MM-YYYY')
textbox2.config(fg='grey')
textbox2.bind('<FocusIn>',on_entry2)
textbox2.bind('<FocusOut>',focus_out2)
textbox2.grid(row=21,column=0,columnspan=1,sticky=E,padx=50)

textbox3=Entry(page3,textvariable=text_input4,font=('bold',10))
textbox3.insert(END,'DD-MM-YYYY')
textbox3.config(fg='grey')
textbox3.bind('<FocusIn>',on_entry3)
textbox3.bind('<FocusOut>',focus_out3)
textbox3.grid(row=23,column=0,columnspan=1,sticky=E,padx=50)


tbox1=Text(f1,height=42,width=100)
tbox2=Text(f1,height=3,width=100)
S= Scrollbar(f1)
S.pack(side=RIGHT,fill=Y)
tbox1.pack(side=TOP,fill=Y)
S.config(command=tbox1.yview)
tbox1.config(yscrollcommand=S.set)
tbox2.pack(side=BOTTOM,fill=Y)

opera1.set("''")
mwin.mainloop()
