## Initial Design Thoughts

fisher.nd.edu, as currently implemented, lends itself well to some kind of semi-static site generation. We need to be able to update content periodically, but it'd be simplest if we could just bang out some Markdown, run a quick build script (maybe even Github Actions to deploy??), and have the results be reflected in the repository as HTML.

Each page of the website is effectively some content sandwiched in between stubs for a header and footer. The home page and a few others are a little bit different, as they have countdowns, instagram embeds, and various photos, but all of this is reasonably doable with minimal extra HTML (could just have special stub files to go on those pages).

It seems like it's worth at least doing some exploratory work to see if we could build a little custom generator to handle the more text-heavy pages. Then we can just dump all the output into a content div or something, center that up, and have things look pretty darn pretty.