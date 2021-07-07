# Project 4: Brevet time calculator with Ajax

Reimplement the RUSA ACP controle time calculator with flask and ajax.

Credits to Michal Young for the initial version of this code.

Author: Warren Liu

## ACP controle times

That's "controle" with an 'e', because it's French, although "control" is also accepted. Controls are points where a rider must obtain proof of passage, and control[e] times are the minimum and maximum times by which the rider must arrive at the location.

The algorithm for calculating controle times is described here (https://rusa.org/pages/acp-brevet-control-times-calculator). Additional background information is given here (https://rusa.org/pages/rulesForRiders). The description is ambiguous, but the examples help. Part of finishing this project is clarifying anything that is not clear about the requirements, and documenting it clearly.

We are essentially replacing the calculator here (https://rusa.org/octime_acp.html). We can also use that calculator to clarify requirements and develop test data.

## AJAX and Flask reimplementation

The RUSA controle time calculator is a Perl script that takes an HTML form and emits a text page in the above link.

The implementation that you will do will fill in times as the input fields are filled using Ajax and Flask. Currently the miles to km (and vice versa) is implemented with Ajax. You'll extend that functionality as follows:

- Each time a distance is filled in, the corresponding open and close times should be filled in with Ajax.
- You'll also implement the logic in acp_times.py based on the algorithm given above. I will leave much of the design to you. You'll turn the implementation that you do. See below for more information.

## Tasks

The code under "brevets" can serve as a starting point. It illustrates a very simple Ajax transaction between the Flask server and javascript on the web page. At present the server does not calculate times. It just returns double the number of miles. Other things may be missing; add them as needed. As before, you should fork and then clone the bitbucket repository, make your changes, and turn in the URL of your repository.

You'll turn in your credentials.ini using which we will get the following:

- The working application.
- A README.md file that includes not only identifying information (your name, email, etc.) but but also a revised, clear specification of the brevet controle time calculation rules.
- An automated 'nose' test suite.
- Dockerfile

## Use

```
docker build .
docker run -d -p 5000:5000 <container_name>
```