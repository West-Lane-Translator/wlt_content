Title: Governance
Status: Hidden
Menu: TopB

{!notice.md!}

[TOC]

### Board Meetings

Board meetings are held on the fourth Wednesday of January,
April, July, and October at 6:00 PM via video conferencing.
Details on how to attend will be sent to
[members]({filename}Membership.md).

The next four scheduled meetings are:

| Date                                      | Time    |
| :---                                      | :---    |
| <div id='meet1'>JavaScript required</div> | 6:00 PM |
| <div id='meet2'>JavaScript required</div> | 6:00 PM |
| <div id='meet3'>JavaScript required</div> | 6:00 PM |
| <div id='meet4'>JavaScript required</div> | 6:00 PM |

<script type="text/javascript">
function setFourthWednesdayOfQuarter(dt) {
    // Calculate the first month of the quarter containing dt.
    var tmp = dt.getMonth();
    tmp = tmp - tmp % 3;
    dt.setMonth(tmp);
    // The earliest possible 4th Wednesday of a month is the 22nd.
    dt.setDate(22);
    /*
      We need to determine when the first Wednesday is from the 22nd.
      In JavaScript dates, Sunday is 0, so Wednesday is 3.  For
      comprehension, here is a table of how many days need to be added
      to the 22nd to get to a Wednesday depending on what day of the
      week the the 22nd is on and the math for calculating it:

       Day of Week of    Days to add to
       the 22nd (DOW22)  get to a Wed.   10 - DOW22   (10 - DOW22) % 7
       ----------------  --------------  -----------  ----------------
            Sunday=0           3         10 - 0 = 10  (10 - 0) % 7 = 3
            Monday=1           2         10 - 1 = 9   (10 - 1) % 7 = 2
           Tuesday=2           1         10 - 2 = 8   (10 - 2) % 7 = 1
         Wednesday=3           0         10 - 3 = 7   (10 - 3) % 7 = 0
          Thursday=4           6         10 - 4 = 6   (10 - 4) % 7 = 6
            Friday=5           5         10 - 5 = 5   (10 - 5) % 7 = 5
          Saturday=6           4         10 - 6 = 4   (10 - 6) % 7 = 4

      Note that the results of the math in the last column match the
      desired results from the second column.
    */
    dt.setDate(dt.getDate() + (10 - dt.getDay()) % 7);
}

function setNextQuarter(dt) {
    dt.setMonth(dt.getMonth() + 3);
}

function setMeetN(dt, n) {
    document.getElementById('meet' + n).innerText =
	dt.toLocaleDateString([], {year: 'numeric',
				   month: 'long',
				   day: 'numeric'});
}

var now = new Date();
var dt = new Date(now);
var i = 1;
do {
    setFourthWednesdayOfQuarter(dt);
    if (now <= dt) {
	setMeetN(dt, i);
	i += 1;
    }
    setNextQuarter(dt);
} while (i < 5);
</script>

[Summaries of past board meetings are available
here.]({filename}Summaries of past board meetings.md)

### Bylaws

Our bylaws are available in [PDF
format]({static}/pdfs/WLT_Bylaws_January_27_2021_distribution.pdf).

### Board Members

| Name              | Office            | Affiliation                                        |
| ----              | ------            | -----------                                        |
| Dennis Hunt       | President Pro Tem | Retired Television Engineer                        |
| Scott Anderson    | Vice President    | Local Resident                                     |
| Chris Sorensen    | Treasurer         | Local Resident                                     |
| Dr. Ralph Garono  | Member            | Local Resident                                     |
| Chris Reid Murray | Member            | Chief Engineer, KKNU / McKenzie River Broadcasting |
| Jeff Williams     | Member            | Local Resident                                     |

Kim Miller, a local resident, is currently performing the duties of
Secretary until we are able to hold an election to fill the position.

We are actively looking for new board members to join us.  Please
reach out to us via our [contact page]({filename}Contact.md) if you
would like to help with the governance of West Lane Translator.

### Technical Committee

| Name              | Affiliation                                        |
| ----              | -----------                                        |
| Dennis Hunt       | Retired Television Engineer                        |
| Chris Reid Murray | Chief Engineer, KKNU / McKenzie River Broadcasting |
