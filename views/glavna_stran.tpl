<h1 class="title">Pozdravljeni na strani kriptovalut. Na voljo vam je:</h1>
<form action="iskanje/" method="get">
<input type="text" name="naslov" value="" />
<input type="submit" value="Išči">
</form>

<ul>
% for kriptovaluta,kratica,leto,url in kriptovalute:
    <li>
        <a href="{{ url }}">
            {{kriptovaluta}}({{kratica}}), Leto ustanovitve: {{leto}} 
        </a>
    </li>
