Title: Testing
Date: 2020-07-13 03:44
Modified: 2020-07-13 03:44
Slug: subdir-test
Authors: Aniruddha Deb

This is a scratchpad of sorts to test the capabilities of Pelican.

Let's start with an Image:
![Test Image]({static}/articles/2020/res/test\_post/big\_buck\_bunny.png)
Big buck bunny looking real handsome ;) Some tweaks have to be made to expand 
the image on click but this is ok for now..

Let's try headings!
# Echo
## Echo
### Echo
#### Echo
##### Echo
###### Echo

looking good, although I will personally never use anything lower than H4 (if 
you're nesting these many headings, you should just go write a book).

Lists looking fine as well:

- This
- is 
- an 
- unordered
- list

Ordered list:

1. Law
2. And
3. Order

Tables (top 10 chess players as of 19th July 2020):

| No | Name | Country | Rating|
|----|------|---------|------------|
| 1 | Magnus Carlsen | NOR | 2863|
| 2 | Fabiano Caruana | USA | 2835|
| 3 | Liren Ding | CHN | 2791|
| 4 | Ian Nepomniachtchi | RUS | 2784|
| 5 | Maxime Vachier-Lagrave | FRA | 2778|
| 6 | Alexander Grischuk | RUS | 2777|
| 7 | Levon Aronian | ARM | 2773|
| 8 | Wesley So | USA | 2770|
| 9 | Teimour Radjabov | AZE | 2765|
| 10 | Anish Giri | NED | 2764|

Some MathJax, and a quote/hyperlink example (this is taken from 
[Math SE](https://math.stackexchange.com/questions/3761395/will-t12-x-substitution-work-for-this-integral/3761410#3761410)):

> let $x = t^{12} \implies dx = 12t^{11} dt$
> $$A = \int \left( \frac{1}{t^4+t^3} + \frac{\ln(1+t^2)}{t^4 + t^6} \right) 12t^{11}dt \\ 
> = \underbrace{\int \frac{12t^8}{t+1}dt}\_{A\_1} + \underbrace{\int \frac{\ln(1+t^2)}{1+t^2}12t^7dt}\_{A\_2} $$
> $A\_1$ can be written as:
> $$A\_1 = 12 \int \frac{x^8 - 1 + 1}{x+1} dx= 12 \int (x^4+1)(x^2+1)(x-1) + \frac{1}{x+1}dx$$
> Which is doable. For $A\_2$, make the substitution $1+t^2 = k \implies 2tdt = dk$
> $$A\_2 = 6 \int \frac{\ln(k)}{k}(k-1)^3dk$$
> This can be integrated by parts as follows:
> $$A\_2 = 6\left( \ln(k) \cdot \left( \frac{k^3}{3} - \frac{3k^2}{2} + 3k - \ln(k)\right) + \int \frac 1k \cdot \left( \frac{k^3}{3} - \frac{3k^2}{2} + 3k - \ln(k)\right) dk\right)$$
> $A\_2$ is also now doable. Add $A\_1$ and $A\_2$ to get $A$ and substitute back till you get $A = f(x) + c$.

Here's an example of some embedded HTML: (using the [chess.com](chess.com) 
chess player to show one of my games)

<iframe id="6878876" allowtransparency="true" frameborder="0" style="width:760px;height:480px;margin:auto;display:block;border:none;" src="//www.chess.com/emboard?id=6878876"></iframe><script type="text/javascript">window.addEventListener("message",e=>{e['data']&&"6878876"===e['data']['id']&&document.getElementById(\`${e['data']['id']}\`)&&(document.getElementById(\`${e['data']['id']}\`).style.height=\`${e['data']['frameHeight']+60}px\`)});</script>

Here's some code to generate a minefield (Taken from the [Mines](https://github.com/Aniruddha-Deb/Mines/blob/master/src/com/sensei/mines/core/MinefieldGenerator.java) repo):
```java
int height = prefs.getRows();
int width = prefs.getCols();
int numMines = prefs.getMines();

for( int i=0; i<numMines; i++ ) {
	boolean put = false;
	while( !put ) {
		int xLoc = (int)(Math.random()*width);
		int yLoc = (int)(Math.random()*height);
		int yDiff = Math.abs( yLoc-y );
		int xDiff = Math.abs( xLoc-x );
		boolean putable = (yDiff > 0) && (xDiff > 0);
				
		if( !(buttons[yLoc][xLoc].hasMine()) && putable ) {
			put = true;					
			buttons[yLoc][xLoc].setMine( true );
		}
	}
}

for( int i=0; i<height; i++ ) {
	for( int j=0; j<width; j++ ) {
		if( buttons[i][j].hasMine() ) {
			padAround( i, j, buttons );
		}
	}
}
```

Everything looks in place! Looking forward to writing some great content here.
Next post: How I migrated from Blogger to github-pages.
