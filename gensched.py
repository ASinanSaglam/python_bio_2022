#!/usr/bin/env python

import datetime, sys

'''Print out schedule.html page. Takes care of all the boilerplate so 
I can rearrange things easily.'''

start = datetime.date(2022,8,30)
end = datetime.date(2022,12,15)
lastassign = 12
noclass = {datetime.date(2022,11,24): "Thanksgiving Break"}

lectures = [
("Introduction/Linux Commandline Basics",[('intro','notes/intro2021.pdf'),'bash',('reference','notes/bash_cheatsheet.pdf')]),
("Linux Commandline File Processing",['bash2']),
("Getting Started with Python",['pythonintro']),
("Systems Biology with <a href='http://pysb.org/'>PySB</a>",['pysb']),
("Control Flow and Basic Data Visualization with <a href='http://matplotlib.org/'>matplotlib</a>",['pyandplot']),
("<a href='http://www.numpy.org/'>numpy</a> Arrays",['numpy']),
("Dictionaries, Sets, and Function Fitting",['numpy2dict']),
("Sequence Analysis with <a href='http://biopython.org/wiki/Biopython'>Biopython</a>",['biopython']),
("More Sequence Analysis",['seqcont']),
("Structure Analysis with <a href='http://prody.csb.pitt.edu/'>ProDy</a>",['prody1']),
("Protein Analysis Continued",['prody2']),
("Molecular Dynamics (<a href='http://www.mdanalysis.org/'>mdanalysis</a>)",['mdanalysis']),
("More Molecular Dynamics",['md2']),
("Clustering",['clustering']),
("Dimensionality Reduction",['dimred']),
("Regular Expressions",['regex']),
("Web Services and Communication Protocols",['web']),
("From Data to Model to the World Web Web",['webprogramming']),
("Cheminformatics (<a href='http://openbabel.org/docs/dev/UseTheLibrary/Python_Pybel.html'>Pybel</a>)",['cheminformatics']),
("Machine Learning with <a href='http://scikit-learn.org/stable/'>sklearn</a>",['machinelearning']),
("EMR with <a href='http://pandas.pydata.org/'>pandas</a>",['emr']),
("Bioimaging I",['bioimaging']),
("Bioimaging II",['bioimaging2']),
("Process Control with <a href='https://docs.python.org/3/library/subprocess.html'>subprocess</a>",['subprocess']),
("multiprocessing",['multiprocessing']),
("Deep Learning",['deeplearning']),
("<b>Project Presentations</b>",[]),
("<b>Project Presentations</b>",[])
]

print ('''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<meta http-equiv="Cache-Control" content="no-store" />
<title>MSCBIO 2025: Schedule</title>
<link href="default.css" rel="stylesheet" type="text/css" />

</head>

<body>
<div class="main">
<h1>Schedule</h1>
<h3>Subject to change</h3>
<h4><a href="https://pitt.hosted.panopto.com/Panopto/Pages/Sessions/List.aspx?folderID=4eac9817-0359-421c-b301-ad91014debc5">Recordings of lectures</a></h4>

<table width=100% style="border-collapse: collapse;">
<thead>
<th>Date</th><th>Topic</th><th>Links</th>
</thead>
<tbody>''')

def linkstr(links):
    '''given list of link information return html string'''
    ret = ''
    ret += "<!--"
    for l in links:
        if type(l) == str: #assume slides
            ret += '<a href="notes/%s.slides.html">slides</a>&nbsp;' % l
        else: # assume typle of name,link
            ret += ' <a href="%s">%s</a>&nbsp;' % (l[1],l[0])
    ret += "-->"
    return ret

day = start
lecpos = 0
assignpos = 0
while day < end and lecpos < len(lectures):
    # is is the monday of the week
    #first assignment and it's not "noclass"
    if assignpos > 0 and assignpos <= lastassign:
        if day in noclass: #no assignment on holiday
            assignpos -= 1
        else:
            print ("<tr class='A'><td>%s</td><td colspan=1>Assignment %d Due 11:59pm</td><td></td></tr>" % (day.strftime('%-m/%-d'), assignpos))
    assignpos += 1
    if day not in noclass:
        lecname = lectures[lecpos][0]
        links = lectures[lecpos][1]
        print ("<tr class='L'>")
        print ("<td>%s</td><td>%s</td>" % (day.strftime('%-m/%-d'),lecname) )       
        print ("<td style='display: inline-block; width: 200px;'>%s</td>" % linkstr(links))
        lecpos += 1
    else:
        print ("<tr class='B'><td>%s</td><td colspan=1>%s</td><td></td></tr>" % (day.strftime('%-m/%-d'), noclass[day]))
        
    if lecpos >= len(lectures):
        break
        
    day += datetime.timedelta(2)
    if day not in noclass and lecpos < len(lectures):
        lecname = lectures[lecpos][0]
        links = lectures[lecpos][1]
        print ("<tr class='R endweek'>")
        print ("<td>%s</td><td>%s</td>" % (day.strftime('%-m/%-d'),lecname))
        print ("<td style='display: inline-block; width: 200px;'>%s</td>" % linkstr(links))
        lecpos += 1
    else:
        print( "<tr class='B endweek'><td>%s</td><td colspan=1>%s</td><td></td></tr>" % (day.strftime('%-m/%-d'), noclass[day]))
  
    if lecpos >= len(lectures):
        break        
    day += datetime.timedelta(5)
        


print ('''</tbody>
</table>
</div>
</body>
</html>
''')
