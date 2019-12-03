<xmp>
<!--CLOCK II-->

<!-- This part can go in the head of the html file -->

<script language="JavaScript" type="text/javascript">
<!-- Copyright 2003, Sandeep Gangadharan -->
<!-- For more free scripts go to http://sivamdesign.com/scripts/ -->
<!--

function sivamtime() {
  now=new Date();
  hour=now.getHours();
  min=now.getMinutes();
  sec=now.getSeconds();

if (min<=9) { min="0"+min; }
if (sec<=9) { sec="0"+sec; }
if (hour>12) { hour=hour-12; add="pm"; }
else { hour=hour; add="am"; }
if (hour==12) { add="pm"; }

document.timeForm.field.value = ((hour<=9) ? "0"+hour : hour) + ":" + min + ":" + sec + " " + add;

setTimeout("sivamtime()", 1000);
}
window.onload = sivamtime;

// -->
</script>

<!-- This goes into the body of the file wherever you want to have the time placed -->

<body>

<form name="timeForm">
 <input type=text" name="field" value="" size="11">
</form>

</body>
</xmp>