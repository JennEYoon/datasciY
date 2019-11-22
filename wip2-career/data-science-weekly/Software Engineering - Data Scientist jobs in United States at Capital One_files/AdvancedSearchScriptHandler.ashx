var states = new Array();
states["Canada"] =  new Array("Ontario","Quebec");
states["Philippines"] =  new Array("Metro Manila");
states["United Kingdom"] =  new Array("England");
states["USA"] =  new Array("California","Connecticut","Delaware","District of Columbia","Florida","Georgia","Illinois","Louisiana","Maryland","Massachusetts","Minnesota","Nevada","New Jersey","New York","Ohio","Oklahoma","Oregon","Pennsylvania","South Dakota","Texas","Virginia","Washington");var cities = new Array();
cities["California"] =  new Array("Irvine","Los Angeles","San Francisco");
cities["Connecticut"] =  new Array("Branford");
cities["Delaware"] =  new Array("Wilmington");
cities["District of Columbia"] =  new Array("Washington");
cities["England"] =  new Array("London","Nottingham");
cities["Florida"] =  new Array("Tampa");
cities["Georgia"] =  new Array("Roswell");
cities["Illinois"] =  new Array("Chicago","Downers Grove","Mettawa","Rolling Meadows","Volo");
cities["Louisiana"] =  new Array("Abbeville","Albany","Alexandria","Bastrop","Baton Rouge","Bossier City","Cameron","Chalmette","Franklinton","Gonzales","Gretna","Hammond","Harvey","Houma","Lafayette","Lake Charles","Larose","Mandeville","Marksville","Marrero","Metairie","Minden","Monroe","New Orleans","Oak Grove","Oakdale","Oberlin","Prairieville","Raceland","Shreveport","Slidell","Sulphur","Tallulah","Vinton","Walker","West Monroe");
cities["Maryland"] =  new Array("Annapolis","Baltimore","Bethesda","Bowie","Chevy Chase","Clarksville","Clinton","Dundalk","Elkridge","Ellicott City","Frederick","Gaithersburg","Germantown","Hagerstown","Hyattsville","Landover Hills","Laurel","Mount Airy","Oxon Hill","Rockville","Silver Spring","Wheaton");
cities["Massachusetts"] =  new Array("Boston");
cities["Metro Manila"] =  new Array("Alabang Muntinlupa City");
cities["Minnesota"] =  new Array("St Cloud");
cities["Nevada"] =  new Array("Las Vegas");
cities["New Jersey"] =  new Array("Caldwell","Closter","East Brunswick","Edison","Fair Lawn","Fairfield","Fort Lee","Freehold","Hightstown","Hoboken","Iselin","Jersey City","Lakewood","Livingston","Millburn","Monmouth Junction","Morganville","Morristown","Newark","Nutley","Paramus","Perth Amboy","Ridgefield","Ridgewood","Secaucus","Toms River","Union","Union City","West New York","Westwood");
cities["New York"] =  new Array("Albertson","Amagansett","Astoria","Babylon","Baldwin","Bay Shore","Bayside","Bellmore","Bohemia","Brentwood","Bronx","Bronxville","Brooklyn","Carle Place","Cedarhurst","Centereach","College Point","Commack","Coram","East Hampton","East Meadow","East Moriches","East Quogue","East Rockaway","East Setauket","Far Rockaway","Floral Park","Flushing","Forest Hills","Franklin Square","Garden City","Great Neck","Greenport","Hampton Bays","Hewlett","Hicksville","Huntington","Huntington Station","Islip","Jamaica","Jamesport","Kings Park","Lake Grove","Levittown","Lindenhurst","Little Neck","Lynbrook","Manhasset","Massapequa","Massapequa Park","Mattituck","Melville","Mid","Middle Village","Mount Vernon","New City","New Hyde Park","New York","Northport","Patchogue","Plainview","Port Washington","Ridgewood","Riverhead","Rocky Point","Ronkonkoma","Roslyn","Sayville","Scarsdale","Smithtown","South Richmond Hill","Southampton","Southold","Staten Island","Sunnyside","Valley Stream","West Hempstead","West Islip","Whitestone");
cities["Ohio"] =  new Array("Columbus");
cities["Oklahoma"] =  new Array("Tulsa");
cities["Ontario"] =  new Array("North York","Toronto");
cities["Oregon"] =  new Array("Tigard");
cities["Pennsylvania"] =  new Array("Philadelphia");
cities["Quebec"] =  new Array("Montreal");
cities["South Dakota"] =  new Array("Sioux Falls");
cities["Texas"] =  new Array("Allen","Arlington","Atlanta","Austin","Bay City","Beaumont","Bridge City","Brownsville","Colleyville","Columbus","Conroe","Corpus Christi","Dallas","Edinburg","Fort Worth","Galveston","Garland","Giddings","Gladewater","Harlingen","Highland Village","Houston","Humble","Irving","Jacksonville","Katy","League City","Lewisville","Lindale","Little Elm","Lufkin","Marshall","McAllen","Mineola","Mission","Nash","North Richland Hills","Orange","Palestine","Paris","Pasadena","Pharr","Plano","Port Arthur","Port Lavaca","Rosenberg","San Antonio","San Benito","Schertz","Schulenburg","Sealy","Southlake","Spring","Sugar Land","Texarkana","The Woodlands","Tyler","Victoria","Webster","Wylie");
cities["Virginia"] =  new Array("Alexandria","Annandale","Arlington","Bailey's Crossroads","Burke","Centreville","Chantilly","Chesapeake","Dulles","Fairfax","Falls Church","Gainesville","Glen Allen","McLean","Richmond","Springfield","Stafford","Sterling","Vienna","Warrenton","Woodbridge");
cities["Washington"] =  new Array("Seattle");var CountriesCities = new Array();
CountriesCities["Canada"] =  new Array("Montreal","North York","Toronto");
CountriesCities["Philippines"] =  new Array("Alabang Muntinlupa City");
CountriesCities["United Kingdom"] =  new Array("London","Nottingham");
CountriesCities["USA"] =  new Array("Abbeville","Albany","Albertson","Alexandria","Alexandria","Allen","Amagansett","Annandale","Annapolis","Arlington","Arlington","Astoria","Atlanta","Austin","Babylon","Bailey's Crossroads","Baldwin","Baltimore","Bastrop","Baton Rouge","Bay City","Bay Shore","Bayside","Beaumont","Bellmore","Bethesda","Bohemia","Bossier City","Boston","Bowie","Branford","Brentwood","Bridge City","Bronx","Bronxville","Brooklyn","Brownsville","Burke","Caldwell","Cameron","Carle Place","Cedarhurst","Centereach","Centreville","Chalmette","Chantilly","Chesapeake","Chevy Chase","Chicago","Clarksville","Clinton","Closter","College Point","Colleyville","Columbus","Columbus","Commack","Conroe","Coram","Corpus Christi","Dallas","Downers Grove","Dulles","Dundalk","East Brunswick","East Hampton","East Meadow","East Moriches","East Quogue","East Rockaway","East Setauket","Edinburg","Edison","Elkridge","Ellicott City","Fair Lawn","Fairfax","Fairfield","Falls Church","Far Rockaway","Floral Park","Flushing","Forest Hills","Fort Lee","Fort Worth","Franklin Square","Franklinton","Frederick","Freehold","Gainesville","Gaithersburg","Galveston","Garden City","Garland","Germantown","Giddings","Gladewater","Glen Allen","Gonzales","Great Neck","Greenport","Gretna","Hagerstown","Hammond","Hampton Bays","Harlingen","Harvey","Hewlett","Hicksville","Highland Village","Hightstown","Hoboken","Houma","Houston","Humble","Huntington","Huntington Station","Hyattsville","Irvine","Irving","Iselin","Islip","Jacksonville","Jamaica","Jamesport","Jersey City","Katy","Kings Park","Lafayette","Lake Charles","Lake Grove","Lakewood","Landover Hills","Larose","Las Vegas","Laurel","League City","Levittown","Lewisville","Lindale","Lindenhurst","Little Elm","Little Neck","Livingston","Los Angeles","Lufkin","Lynbrook","Mandeville","Manhasset","Marksville","Marrero","Marshall","Massapequa","Massapequa Park","Mattituck","McAllen","McLean","Melville","Metairie","Mettawa","Mid","Middle Village","Millburn","Minden","Mineola","Mission","Monmouth Junction","Monroe","Morganville","Morristown","Mount Airy","Mount Vernon","Nash","New City","New Hyde Park","New Orleans","New York","Newark","North Richland Hills","Northport","Nutley","Oak Grove","Oakdale","Oberlin","Orange","Oxon Hill","Palestine","Paramus","Paris","Pasadena","Patchogue","Perth Amboy","Pharr","Philadelphia","Plainview","Plano","Port Arthur","Port Lavaca","Port Washington","Prairieville","Raceland","Richmond","Ridgefield","Ridgewood","Ridgewood","Riverhead","Rockville","Rocky Point","Rolling Meadows","Ronkonkoma","Rosenberg","Roslyn","Roswell","San Antonio","San Benito","San Francisco","Sayville","Scarsdale","Schertz","Schulenburg","Sealy","Seattle","Secaucus","Shreveport","Silver Spring","Sioux Falls","Slidell","Smithtown","South Richmond Hill","Southampton","Southlake","Southold","Spring","Springfield","St Cloud","Stafford","Staten Island","Sterling","Sugar Land","Sulphur","Sunnyside","Tallulah","Tampa","Texarkana","The Woodlands","Tigard","Toms River","Tulsa","Tyler","Union","Union City","Valley Stream","Victoria","Vienna","Vinton","Volo","Walker","Warrenton","Washington","Webster","West Hempstead","West Islip","West Monroe","West New York","Westwood","Wheaton","Whitestone","Wilmington","Woodbridge","Wylie");
/*
     FILE ARCHIVED ON 16:54:00 Jan 06, 2015 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 18:08:21 Nov 22, 2019.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  exclusion.robots: 0.131
  PetaboxLoader3.datanode: 149.985 (4)
  load_resource: 71.833
  esindex: 0.007
  RedisCDXSource: 4.118
  LoadShardBlock: 140.681 (3)
  exclusion.robots.policy: 0.121
  PetaboxLoader3.resolve: 48.9
  CDXLines.iter: 18.621 (3)
  captures_list: 167.329
*/