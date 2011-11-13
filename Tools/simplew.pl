# checks source files with word-forms and 
# finds words with single VOCAL char but without accent
# created 2011-11-14
#

use strict ;
my $infile = "../Data/Collected/RussianWords_AllForms_Accents_86xxxBases_cp1251.txt" ;

open(INFILE,"<$infile") || die "cannot open $infile\n" ;
open(OFILE,">x.txt") || die "cannot open file x.txt\n" ;

while(<INFILE>) 
{
	chomp ;
	s/^.*#(.*)$/$1/ ;
	my @words = split(/,/) ;
	my $w ;
	foreach $w (@words)
	{
		next if $w =~ /['`]/ ;
		next if $w =~ /¸/ ;
		print OFILE "$w\n" ;
	}	
}

close(OFILE) ;
close(INFILE) ;