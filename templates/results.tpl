<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="/styles/bootstrap.css" type="text/css">
<link rel="stylesheet" href="/styles/results.css" type="text/css">
<link rel="stylesheet" href="/styles/bootstrap-responsive.css" type="text/css">
<title>DaveDaveFind: {{ search_query }}</title>
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-30777226-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
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
			<div class="span6">
		<h2>You searched for: <strong class="orange">
		%for word in query_string_words:
		<a href="/search?search_query={{ word }}">{{ word }}</a>
		%end
		</strong></h2>
		%if not results:
			<p>No results found for {{ search_query }}. Try clicking on one of the individual terms above.<p>
		%end
		</div>
		</div>
		%if pyterm_info:
		<div class="row">
		<div class="span6 well">
			%if pyterm_info['code']:
			<p><a href="{{ pyterm_info['url'] }}"><code>{{ pyterm_info['code'] }}</code></a></p>
			%end
		<blockquote>{{ pyterm_info['desc'] }}</blockquote>
		<p class="source">Read more: <a href="{{ pyterm_info['url'] }}"><img class="icon" src="/styles/py.png" height="15" width="15">  Python documentation</a></p>
  		<ul class="nav nav-list">
  		<li class="divider"></li>
		<li><p class="pull-right">Python search powered by <a href="http://duckduckgo.com/"><img class="icon" src="/styles/ddg.png" height="15" width="15"> DuckDuckGo</a></p></li>
		</ul>
		
		
		

		</div>
		</div>
		%end
		<div class="row">
		<div class="span5" id="fixed">
			%if video_dicts:
				<div>
				<h2>Videos:</h2>
				%for video in video_dicts:
				<div class="results well">
				<strong>{{ video['title'] }}</strong>
				<p><a href="{{ video['url'] }}">{{ video['url'][:70] }}</a></p>	
				<iframe width="430" height="248" src="http://www.youtube.com/embed/{{ video['id'] }}?rel=0&start={{ video['start'] }}&wmode=transparent" frameborder="0" allowfullscreen></iframe>			
				</div>
				%end
				</div>
			</div>
			%end
			<div class="span7">
			%if page_dicts:
				<div>
				<h2>Webpages:</h2>
				%for page in page_dicts:
				<div class="results well">
				<strong>
					%if page['doc']:
					[PDF] 
					%end
				{{ page['title'] }}</strong>
				<p><a href="{{ page['url'] }}">{{ page['url'][:70] }}</a></p>
					%if show_daverank:
					<p><code>DaveRank: {{ page['daverank'] }}</code></p>
					%end
				<p>{{ page['text'] }}…</p>				
				</div>
				%end
			%end
				</div>
			</div>
		</div>
	</div>
</div>
</body>
</html>