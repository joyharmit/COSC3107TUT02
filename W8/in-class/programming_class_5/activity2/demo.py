import pyhtml
import student_x_page_1
import student_y_page_1

pyhtml.need_debugging_help=True

#All pages that you want on the site need to be added as below
pyhtml.MyRequestHandler.pages["/"]        =student_x_page_1   #Page to show when someone accesses "http://localhost/"
pyhtml.MyRequestHandler.pages["/studenty"]=student_y_page_1   #Page to show when someone accesses "http://localhost/studenty"

#Host the site!
pyhtml.host_site()