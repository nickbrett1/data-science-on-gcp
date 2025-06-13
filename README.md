# data-science-on-gcp (fork)

Here is source code from the excellent book:

<table>
<tr>
  <td>
  <img src="cover_edition2.jpg" height="100"/>
  </td>
  <td>
  <a href="https://www.amazon.com/Data-Science-Google-Cloud-Platform/dp/1098118952/">Data Science on the Google Cloud Platform, 2nd Edition</a> <br/>
  Valliappa Lakshmanan <br/>
  O'Reilly, Apr 2022
  </td>
  <td>
  Branch <a href="https://github.com/GoogleCloudPlatform/data-science-on-gcp/">2nd Edition</a> [also main]
  </td>
</tr>
<tr>
  <td>
  <img src="https://images-na.ssl-images-amazon.com/images/I/51dgw%2BCYSOL._SX379_BO1,204,203,200_.jpg" height="100"/>
  </td>
  <td>
  Data Science on the Google Cloud Platform <br/>
  Valliappa Lakshmanan <br/>
  O'Reilly, Jan 2017
  </td>
  <td>
  Branch <a href="https://github.com/GoogleCloudPlatform/data-science-on-gcp/tree/edition1_tf2">edition1_tf2</a> (obsolete, and will not be maintained)
  </td>
</table>

It walks through an end-to-end example for ingesting and cleaning data and using that to make a predictive model. 

### Changes and additions made
I made a few changes and additions to the code as I went through the book:

1. Added support for a vscode development container. This allows for the necessary client side environment to be automatically setup, specifically:
    1. All the necessary python packages are installed. Only tensorflow is pinned (@2.12) as newer versions didn't work. 
    2. The latest gcloud SDK package is downloaded, installed from google.com and added to PATH
    3. A .boto file is added that allows faster GSUtil uploads and removes some warnings 
    4. Postgres client and graphviz are installed
    5. Login to gcloud is run on container creation, and appropriate region and project set, saving some keystrokes
    6. Added a .gloudignore that prevents accidently uploading some of the generated json files
    7. I added my favorite shell (zsh) and extensions
2. Upgraded the code to use Google Cloud Functions
3. Fixed parameters to address failures as they came up, e.g. gloud functions deploy needed a higher memory limit (--memory 500MiB)
4. Fixed a few bugs in the beam streaming code, use of timezone_at and ensuring (float) conversion
5. Fixed some of the AutoML tuning code from Chapter 10

### Purchase book
[Read on-line or download PDF of book](https://www.oreilly.com/library/view/data-science-on/9781098118945/)

[Buy on Amazon.com](https://www.amazon.com/Data-Science-Google-Cloud-Platform-dp-1098118952/dp/1098118952/)
