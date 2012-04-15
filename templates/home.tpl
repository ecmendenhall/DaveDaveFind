<!DOCTYPE html>
<html itemscope itemtype="http://schema.org/Product">
<head>
<script src="/styles/jquery-1.7.2.min.js" type="text/javascript"></script>
<script src="/styles/bootstrap-dropdown.js" type="text/javascript"></script>

<link rel="stylesheet" href="/styles/bootstrap.css" type="text/css">
<link rel="stylesheet" href="/styles/home.css" type="text/css">
<link rel="stylesheet" href="/styles/bootstrap-responsive.css" type="text/css">
<meta itemprop="name" content="DaveDaveFind">
<meta itemprop="image" content="http://davedavefind.appspot.com/">
<title>DaveDaveFind</title>
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
<ul class="nav pull-left" data-no-collapse="true">
  <li class="dropdown" data-no-collapse="true">
    <a href="#"
          class="dropdown-toggle"
          data-toggle="dropdown">
          About
          <b class="caret"></b>
    </a>
     <div class="dropdown-menu infobox" data-no-collapse="true"><p><strong>DaveDave<span class="orange">Find</span></strong> was built by <a href="http://twitter.com/ecmendenhall/">@ecmendenhall</a> with lots of help from <a href="http://www.udacity.com/">Udacity</a> and <a href="http://www.cs.virginia.edu/~evans/">David Evans</a>. You can learn to make your own search engine in <a href="http://www.udacity.com/overview/Course/cs101">CS101</a>, read more about this project on its <a href="http://davedavefind.tumblr.com/">development blog</a>, or see the code on <a href="http://github.com/ecmendenhall/DaveDaveFind">GitHub</a>.</p>
      <p>The search crawler and web application were written in <a href="http://python.org">Python</a>, using the <a href="http://bottlepy.org/docs/dev/">Bottle</a> web framework on <a href="https://developers.google.com/appengine/">Google App Engine</a>. The crawler code uses <a href="http://www.crummy.com/software/BeautifulSoup/">BeautifulSoup</a> to read HTML, <a href="http://nikitathespider.com/python/rerp/">Nikita the Spider</a> to read robots.txt files, and the <a href="http://duckduckgo.com/api.html">DuckDuckGo API</a> to search Python documentation. Pages are styled with <a href="http://twitter.github.com/bootstrap/index.html">Twitter Bootstrap</a> and enhanced by <a href="http://glyphicons.com/">Glyphicons</a>.
      </div>
  </li>
  <li class="dropdown" data-no-collapse="true">
    <a href="#"
          class="dropdown-toggle"
          data-toggle="dropdown">
          Help
          <b class="caret"></b>
    </a>
      <div class="dropdown-menu infobox" data-no-collapse="true"><p><strong>DaveDave<span class="orange">Find</span></strong> searches the full-text of the <a href="http://udacity.com/">Udacity website</a>, <a href="http://www.udacity-forums.com/cs101/">CS101 forums</a>, course documents, and lecture transcripts. It supports multi-word lookup (but sometimes delivers better results for single words).</>
      <p>If your search query is found in a video transcript, it will try to link inside the video to the moment the query occurs. If your search query is a common Python-related term, it will try to look up information in the Python documentation. Try searching for the name of a built-in function or standard library module, like <code>str</code> or <code>urllib</code>.</P>
      <p>The search box also accepts commands inspired by <a href="http://duckduckgo.com/bang.html">bang syntax</a>. Try typing <code>--forum</code> before your search query to search the CS101 discussion forum, <code>--python</code> to search Python documentation, or <code>--daverank</code> to show the DaveRank‌™ for each result underneath its URL.</p> 
      </div>
  </li>
  
</ul>
<div class="pull-right">
<a href="https://twitter.com/share" class="twitter-share-button" data-text="DaveDaveFind: the search engine Udacity promised!" data-related="ecmendenhall">Tweet</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
<g:plusone size="medium"></g:plusone>
<script type="text/javascript">
  (function() {
    var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
    po.src = 'https://apis.google.com/js/plusone.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
  })();
</script>
</div>
</div>
</body>
</html>