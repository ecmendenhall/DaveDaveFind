<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="/styles/bootstrap.css" type="text/css">
<style>

body { padding-top: 60px; }
.orange { color: #F7A900; }

.navbar h2 a { color: #ffffff; }
.navbar-form { margin-top: 10px; }


.navbar-inner {
  background-color: #686868;
  background-image: -moz-linear-gradient(top, #686868, #333333);
  background-image: -ms-linear-gradient(top, #686868, #333333);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#686868), to(#333333));
  background-image: -webkit-linear-gradient(top, #686868, #333333);
  background-image: -o-linear-gradient(top, #686868, #333333);
  background-image: linear-gradient(top, #686868, #333333);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#686868', endColorstr='#333333', GradientType=0);
}

</style>
<title>DaveDaveFind: {{ search_query }}</title>
</head>
<body>
<div class="navbar navbar-fixed-top">
<div class="navbar-inner">
<div class="container">
		<span class="brand">
		<h2><a href="/">DaveDave<strong class="orange">Find</strong></a></h2></span>
		<form class="navbar-form form-inline" action="/search" method="GET" >
  				<input type="text" name="search_query" class="input-xlarge">
  				<button type="submit" class="btn btn-warning"><i class="icon-search icon-white"></i></button>
		</form>
</div>
</div>
</div>

<div class="container">
		<div class="row">
		<div class="span6 offset3">
			<h3>You searched for: {{ search_query }}</h3>
			%if results:
				%for page in results:
					<a href="{{ page.url }}">{{ page.url }}</a>
			%end
		</div>
	</div>
</div>
</body>
</html>