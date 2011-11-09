use strict ;

open(INFILE,"<RussianWords_AllForms_Len_Accents_cp1251.txt") || die " cannot open file\n" ;
my $cnt=0 ;
my %line ;
while(<INFILE>)
{
	chomp ;
	if(defined $line{$_})
	{
		$line{$_}++ ;
	}
	else
	{
		$line{$_}=1 ;
	}
	$cnt++ ;
}

close(INFILE) ;
print "Total lines read: $cnt\n" ;
my $size = keys %line;
print "Unique lines: " . $size . "\n" ;
my $l ;
open (OUTFILE,">duplicated.txt") ;
foreach $l (keys(%line))
{
	print OUTFILE "$l: $line{$l}\n" if $line{$l} >1 ;
}
close(OUTFILE) ;