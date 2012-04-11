<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="/styles/bootstrap.css" type="text/css">
<style>
.container { margin-top: 20%; }

.orange { color: #F7A900; }

.well {
  background-color: #686868;
  background-image: -moz-linear-gradient(top, #686868, #444444);
  background-image: -ms-linear-gradient(top, #686868, #444444);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#686868), to(#444444));
  background-image: -webkit-linear-gradient(top, #686868, #444444);
  background-image: -o-linear-gradient(top, #686868, #444444);
  background-image: linear-gradient(top, #686868, #444444);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#686868', endColorstr='#444444', GradientType=0);
}

.credits { 
	color: #ffffff;
	opacity: .9;
	font-size: 87%;
}

.credits a { 
	color: #ffffff;
	opacity: .9;
	color: #F7A900;
}

.credits a:hover { text-decoration: none; }

#searchbox{ float: left; white-space: nowrap; }

.navbar p { padding-top: 5px;}


.navbar-inner {
  background-color: #686868;
  background-image: -moz-linear-gradient(top, #686868, #444444);
  background-image: -ms-linear-gradient(top, #686868, #444444);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#686868), to(#444444));
  background-image: -webkit-linear-gradient(top, #686868, #444444);
  background-image: -o-linear-gradient(top, #686868, #444444);
  background-image: linear-gradient(top, #686868, #444444);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#686868', endColorstr='#444444', GradientType=0);
}

.twitter-share-button { padding-top: 5px; }

</style>
<link rel="stylesheet" href="/styles/bootstrap-responsive.css" type="text/css">
<title>DaveDaveFind</title>
</head>
<body>

<div class="container">
	<div class="row">
		
		
		<div class="span6 offset4">
		
		<h1>DaveDave<strong class="orange">Find</strong></h1>

		<form action="/search" method="GET" id="searchbox" class="well form-search">
  				<input type="text" name="search_query">
  				<button type="submit" class="btn btn-warning"><i class="icon-search icon-white"></i></button>
			</form>

		
			
		</div>
	</div>
<div class="navbar navbar-fixed-bottom">
<div class="navbar-inner">
<div class="container">
<div class="pull-left">
<p class="credits">Built by <a href="http://twitter.com/ecmendenhall/">@ecmendenhall</a> with help from <a href="http://www.udacity.com/">Udacity</a>. Make your own in <a href="http://www.udacity.com/overview/Course/cs101">CS101</a>.</p>
</div>
<div class="pull-right">
<a href="https://twitter.com/share" class="twitter-share-button" data-via="ecmendenhall">Tweet</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
</div>
</div>
</body>
</html>