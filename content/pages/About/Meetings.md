Title: WLT Board Meetings

Board Meetings Dates Scheduled: Historically, meetings were held on the
fourth Wednesday of January, April, July, and October at 6:00 PM in
the Bromley room of the Siuslaw Public Library. Due to COVID-19
limitations, it is unclear when the next meeting will occur and in
what format.

### Next Meetings:

Date | Time | Location
---- | ---- | --------
<div id='meet1'>JavaScript required</div> | 6:00 PM | Cancelled due to COVID-19 limitations
<div id='meet2'>JavaScript required</div> | 6:00 PM | TBD
<div id='meet3'>JavaScript required</div> | 6:00 PM | TBD
<div id='meet4'>JavaScript required</div> | 6:00 PM | TBD

<script type="text/javascript">
function setFourthWednesdayOfQuarter(dt) {
    // First, calculate the first day of the quarter
    var tmp = dt.getMonth();
    tmp = tmp - tmp % 3;
    dt.setMonth(tmp)
    dt.setDate(1);

    dt.setDate(22) // The 22nd is the earliest possible 4th Wednesday
    /*
      We need to determine how many days out Wednesday is.  Sunday is
      represented as Day 0, so Wednesday is Day 3.  For comprehension,
      here is a table of how many days need to be added to the current
      date to get to a Wednesday and what the code does:

       Current       Needed   10-Current   (10-Current)%7
       Sunday(0)       3          10              3
       Monday(1)       2           9              2
       Tuesday(2)      1           8              1
       Wednesday(3)    0           7              0
       Thursday(4)     6           6              6
       Friday(5)       5           5              5
       Saturday(6)     4           4              4
    */
    dt.setDate(dt.getDate() + (10 - dt.getDay()) % 7)
}

function setNextQuarter(dt) {
    dt.setMonth(dt.getMonth() + 3)
}

function setMeetN(dt, n) {
    document.getElementById('meet' + n).innerText =
	dt.toLocaleDateString([], {year: 'numeric',
				   month: 'long',
				   day: 'numeric'})
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
