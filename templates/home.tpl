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


</style>
<title>DaveDaveFind</title>
</head>
<body>
<div class="container">
	<div class="row">
		<div class="span6 offset3">
		<h1>DaveDave<strong class="orange">Find</strong></h1>
		</div>
	</div>
	<div class="row">
		<div class="span6 offset3">
			<form action="/search" method="POST" class="well form-search">
  				<input type="text" name="search_query" class="input-xlarge">
  				<button type="submit" class="btn btn-warning"><i class="icon-search icon-white"></i></button>
			</form>
		</div>
	</div>
</div>
</body>
</html>