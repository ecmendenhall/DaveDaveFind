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

#searchbox{ float: left; white-space: nowrap; }

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
	
</div>
</body>
</html>