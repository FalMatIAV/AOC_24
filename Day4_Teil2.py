def count_x_mas_occurrences(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    found_patterns = []

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_x_mas(x, y):
        # Check for the X-MAS pattern in a 3x3 grid
        if is_valid(x, y) and is_valid(x + 2, y + 2):
            # Extract the 3x3 grid
            subgrid = [grid[x + i][y:y + 3] for i in range(3)]
            # Check for "MAS" or "SAM" in the shape of an X
            if (subgrid[0][0] == 'M' and subgrid[1][1] == 'A' and subgrid[2][2] == 'S' and
                subgrid[0][2] == 'M' and subgrid[2][0] == 'S') or \
               (subgrid[0][0] == 'S' and subgrid[1][1] == 'A' and subgrid[2][2] == 'M' and
                subgrid[0][2] == 'S' and subgrid[2][0] == 'M') or \
               (subgrid[0][0] == 'M' and subgrid[1][1] == 'A' and subgrid[2][2] == 'S' and
                subgrid[0][2] == 'S' and subgrid[2][0] == 'M') or \
               (subgrid[0][0] == 'S' and subgrid[1][1] == 'A' and subgrid[2][2] == 'M' and
                subgrid[0][2] == 'M' and subgrid[2][0] == 'S'):
                return True
        return False

    for i in range(rows - 2):
        for j in range(cols - 2):
            if search_x_mas(i, j):
                count += 1

    return count, found_patterns

# Reference input string with at least 9 sure patterns
input_string = """
MSSMSAMXSAMASMSMSAMMMMMMMXSXSMMSAMXSSSMXMSMMSMXMXSXMMSAMXMSSSSSSMSASMSSMSAMXMSMXSXSMMMXSSMAMXXMXSXMAMSAMXXMXAXXSASAMXMMAMMSSXSXMMXSMMXSXXMXX
AAMAMXAMMAMSAAAAMAMAAAAMMAMMSAAXAAMAAAMAXAMAAAAAASAMXSXMASMAXMAAMMASMAAAMAMAMAAMSAXAAXMXAXMASXSAMASAMXSSMMSSSMASAAAXMASMMAAMMMAMSMSASMSXAMAM
MMSSXSSSSSMAMSMSMMMXXSSSMXSAMMMMAXMMAMSXSSSXMSMMXSAMXMAMXXMMMMSMMXAXMXMSMASASMSMXASMMXMSAMMAMXMASAMXSMXMXAAAAXMXASMMMMSAMMXXAMAMAASAMAXSAMXA
XXAXAXAAAMXMXXAXAMSSMMXAMAMASASAMXMXAXAAAAAMXAMSASXMASMMMMAMAXAXMMMSSXMXMXSXSAMXXAMMAXMAMMSSSXSAMMXXAMXAASMXMMXMMMMASXSAMXSSSSSSMXMAMSMSMAMX
XXMMMMMMMMMXMMMMSMAAAASAMXSXMAXMAXMSSSMMMMMMSASMMXAXASAAXXSSSXSASXMAXAMMSMMAMAMASXMXSXXAXAXAAXMASXSSSSMSMXSSXAAXAASAMXSXMMAAAAMAXSXXXAAXAAXA
SMXSXXXAAAAAXSMAMMSXMMSAMXAMMMMXAAMAMAXMXMAMSXMAMSSMASXMSMXAXAMSMAMASXMAXAXMMAMXMXASAMSSMMMMMMXXMAAAAMAXXAMXXSMSSMMXSXMAXAMMMMMMMMAXSSXMSASM
SASMMAASXSSMAAMXMAXSXMSAMAXMASXMSSMASXMAMSMXSASXMAMMAXAXSXMAMSMASXMXMMMMSXMMSSSSSSMMAXAXAASMASXSMMMMMMMMMSSMMAXAXXSMAAXAMSMMXMXXAMXMAMMMAAAX
XXAAMXMMAMMMSXMXMASAMXSASMMSASXMAXMAMMASAMMASAMXMAXMMSMXMASXMASMMXMMMMAAXMMXAXMAAAMMXMAXMMAXAMXMAXXASAMXAMAMSAMXSXAXSSMXMXASXMMSMMXMASAMMMMX
MSSXMSXMASXMMASXMMXASASXMAXMXMAMXSMXMSAMASXXMMMXMSXSMXXASAMSSXMMSAMAAMMSMMXMASMMXMMMAMXMSAMMMSMMASMMSAXAXSAMMASAMMMMXXAMSMMMAAAAAMXMASASXXXX
XAAXSXXSAMAXXAMXASXMMAXXMSMMMSMMAXMAMMAMAMXAAMMSAXAMMMSMXMSMXAMASMSSSSSXMMAMSMXMSXMSAMXAMMXMXAMXAAAASMMMMSAMXAMMSAXSAMXMAAASMMMSSMAMASMMMXMM
MAXMSAMMMSMMMSMSAMAMMMMXMASAAAXXSAMXMMSMSSSSSMMSAMXMAAAAXSAMSMMASAAAXMAXMAMMMMAMAXMMSMMAASAMMXMMSSMMMXAAAMXSAMXXSXSAMXSSSSMSMSAAXMXMAXMAXASX
AMSAMXMAMAMAXAAMXSXMAAXMMASMSSSMMXSXXSXAAAXXAAAXASASMMSSMMAMXXMASMMSMMAMSAMAAXSSMMSAAXMMMMASAMXAAAAMXSSXXXAXAMMMMMMAAAXMAMAMAMMSSMSSXMSMSASM
MSAMSMSMSASXSMXMASAMSMSAMMSAAAAAAASMMXAMMSMSSMMMXMAXAXXMAMSMMSMMXAMXMAMXSASMSSMAXAMMSSMAXSAMXAMMSSMMMXMASMMMAXSAAAMAMSMSSMSMAMMAAAAAAMAAMAMX
XAAXXASAMMSAAMXMASAMASMXMAMMMSMMMXSASASMSXAAMAMXSMAMSAMXSAAAXAXXXXMSSSSMSAMMMAMAMXSAAAXXMMAMXSSMMAMMAMXAMAMMSXSSSSSMAMAXMAMXMXSMMMMSSMMSMAMM
MMAMMMMAMAMXSMMMXSAMXSMXMAXMAMXXMXSAMAXXXMMMMSMAXAXAMASAXMSMMSSMSSXAAAXXMAMXSAMXAXMMXSMSMXSMMXAXSAMMSAMSSMSAXAMAMAAAAMSMMSMMSASXXMAMAMXAMAXM
XMMMAAAAMASXXAXSMMASAMXXSMMMAXMXSMMAMXMAASXMAXMMMMMASXMASAXXMASMAMMMSMMMSAMMXMSSSXXSSXMXMAXAXSMMSXMXMAXMAXMASMMAMSMMMSMASAMAMASXAMXSAMXAMXSM
XMASMMSSSXSAMXMXAAXMXSAXAMASMXSASASAMMMSMXAMAXAXAXXASASAMXMMMMSMAMAXAXAXSASMAAXAXAXSAXSAMXSMMMSMXMSSMSSSSMMAMASXXMXMMAXMMASAMSMMXSMSASMXSMAX
SSMSAMXAMXMXMASMMMMMXSXSMSASAAMASAMXMXAMXSMMASXMMSMASAMXAMXSAXXMASXSSMMXMMAXXMMAMXMMAMSMSXAAAAAXAAMAAAAXMAMXSAMXMXAXMMXSSMMMMMXMASXMAXAAAAXS
XAXMAMMASAAMSMXAAMAXMXMAMMXMMSMMMAMMSMASAXAAXXMAAAMMMAMXXMSMXSAMXMAAXAXAMMSXSAMSMXXXMMSAMXMXMSSSXSMMMMSMSSMMMMSASXMMASMMAXXAAMAMASAMXMMXSSMA
MSMMAMXAMXMXAMSMMMMSMSSMXSSMXMASXXMAXMAMASAMSMSMMMXAMSMAMSAMMSXSMSMMMSMAXAXAXMXAXMXMXAXAAXXXMXMXAMMSSMAASMMAAASMSAXSAAASXMSMXXAMAXMAXAMAMXAM
AAXXSAMXSASXXMAMMSXAMAAXMAAXMXAAMMMSSMXSASAXAXAMXMMMMAMSXSASAXASAAXXAXSSMAMAMXSSSMAXMSSSMMMMSAMMSMAAASMSMSMMMXSMSAMXMSMMMMAXMSMMMMXSSSMASMSM
SASXMASASASAXXASAMSSMSSMMXSMMMSMMAAMAMAMASMSSXMSSMASXMSXAMXMMMSMSMSMMMAXMXMAMXXXAMAMMMAAMSMAMAMAXMMSMMXMXAXSSMSAMMMMMMMAMSAXXASAMXMMAASAXAAS
MASXMASAMXMAMSAMXMAXMAMXSAMMSAXASMXSAMXMXMAAAASAMAAXAMMMXMMMXMMAAXXAMAMXMASASXMSMMSSMAXMMMMXSSMSSXXXAXMMXXXMAXMMMSSXAXSAMMXXSASMSAMMSMMXXSAS
MAMXMXXAXXMAMAXAMMXSSSSMMASAMSSMMAASXSXMXMMMSMMASMMSSMAASXSMAXMSMSMMMAXAMASMSAMXAAAAXXMMXSMAAAAAAXMSXMASMSAXSMMMMAXXXMSAXSAMMXMASMSMMXSSXMAS
MMMMSMSSMMXMSMMMMMMMMAMASAMAMAXXMMMMASMXAXMXMAMXMAMXXSMXMAASASMMAMAASXXSAMXASXMMMMSSMSAMAAMMSMMMSMMAMASXAXXAMXXAMXSXSAMAMMAXSAMXMXXMMAMXXMXM
XXMAAAAASXXMAXAAAAAAMAMAMXSXMSSSXSXMSMMSSMSAMXMMMSASAMXMMMMMXAAMMMMMSAAMXSMMMMSXAXMXAXAMSSXMXXXMAXXAXSXXMASMXMXASAMXSAMSXSMMXXSAAXSAMASXXMAS
XSXSMMMSXXASMSXSMSSXSAMAXMXMMMAAXSAMAAAAXMMAMSMMAXAAXMAXSSSSSSXXXAXAMXMMSXMXAAMXMMMMSMAXXXMXMMMSMXSMSXXASAMMAMASMXMAMMMMAAXXMASASMSMSASMASAM
MAMMAMSXMSAMXXAXAAAAAXMSMMAXSMMMMSAMSMMSSSMAAAMSMMXMXMXSAAAMAMXSSMSMSMASMAMSMMSASAMXAMXMMMMAAAAAMXXSAXSMMMMSAMMAAXSMMAAMMMAXMXMXMASXMAXXAMAS
AMASAMMMMSAMASAMMMMMMMXMASXMXXAAAMAMXAMAAASMSXMXXXAMMASMMSSMMMSXSAAAMXXAXAMAMXSASAXSAXXMAASXSMSSMAMAMMXXAMAMMSXMXMSASXMXSMMXXASMSMMAMXMMMSSM
XXMAXSAAASAMXAAMXXMAAXASAMASXMMMSSSMSMMMSMXMXMMMXXXXAMXXAXAXXMXAMSMSMMSMSXXASMMMMXMMAMXSSXSXXMAXMAXMXAMXMMAMMAMXMASAMXSAAASMSASMSAMXMXMAMXXX
SSSMASXSMSMMSMASXXXXAXXMASAMAXXAMXMXXXSXXXMMMAAXMAMASMMMMSMMMMMAMAXAXAXXAMXMXXAAMASXXSAMXASASASMSMSXXSMASMMMMAMMAMMMMAMMSMAAMASASAMASAMMXMXM
SAAAASAMAXXAMXAXMASMAMAMAMMSAMASMMSSMAMASMMASXMXAAAXXAAAXAAASMMMSXSSMSSMMMASMSMMSASAMMASMMMAMXMAXMAXMXMAXAAXXAMXXMAXMAMMMXMXMAMMMASXMAMSASMA
MSMMMSAMAMMSSMMSAMAAXAAMMSAMAMXMAXAAMMMXMAXAMAAXSXSAMSSMMMMMXAAASMXAAAXAXMXSAAAXMASAXSXMAMMMMSMXMXMAXAMSSMMXSAMSASXMASAMXASXMASMSAMMMAMSAMAS
AASAAMMMXMAMAMAAMSXSMSMSMMASXMSSXMSMSASASXMSSMMMMAAAXAXXSSSSSSMMSASMMMSXMASMMMMMMXSXMAXMAMXMXMAMMMSSMXXAAXAXMAMXAMASAMXAXSMXSAXXAAASXSAMXMSM
SMSMMSASXMASXMMMXXAMAAXMXSAMXMAAXXMASMSAMMSMAAMAXMSAMXSXSAAAMXAAXMASAAAAXXMASMMSMAXAAMSSMAMMAAXMAMXXXMASXMSSMSMXXSAMAMXSXMAXMASAMXXAAMMXAMAM
AXXAMMAAMSXMAXXXSSSSSXXMAMXAAXSMMXMASMMXMMAMSMMSMXMAAXAMMMMMMMXMXXAXMSMMMSAMXAASMSMSSXAAMSASXSSSSSMAXMAXAAXXAXAXXMMXXMAMMMSMMASXAMMMSMMSMSAS
MMMSMMAMXMASXMSXAAAAXXMMSSMMAMXXMXMMMMAAXXAXAAXAAAMAMMXSAMXMASMSSMSMMMASAXXAMAMSAAAXMMSXMMMAMXXAASMMSXAXMSMMXMXMXMAMSMXSAXMAXAXXSXAAXAXSXSXS
XSAMAXXXAMAMAAAMMMMMMASAMAXSSXSAMXXMAMSSMMXSAMXMXSAMXMASASXXMASAXAAXASAMSMSXMSXMMMSMSAXASMSMMMMMMMXASMXSAXMSASMSAAAAXAMMMSSMMXSMMXMSSMMMMMMS
XMAXAMXSXMXSMSMMAAAAXMMAXAMAMXMAMAASXMXAXAMMMXAXAMXSMMASAMMXXMMSMSMSXMAMXXSAAMAMSXAAMASMMAAXMXAXAXMAXAMMAMSAMXASMSMSMXXAAMAAMSAMXXSAMXAAAAAX
MMSMASXMMMAMXMASXMSSMXSSMSXMAMSAMXXAASMMMXSAASMMXXMAXMASXAMSXSAXMMASAMXMMASXMXAMXSMSMAMMMSMSSSMXMSASMSMMAMXMXMXMXXXMASMASXSMMASAMMMAMSSSSSSM
MAXSAXAXAMAMASMMSAXXAMAMAMMXSMSASXMXAMAAAASXMASMXSAMXMAXXAAXXMASASASMMMAMMMMMSSXMASAMXSXAAXAAAXSXXAXAXMSMSMXMSAXSXAMMASXMAMXSMMMSASAMXMAAAAA
MAMMXSMMSSSSMSAAXMAMMMAMAMXAMXSAMMSASMSMMMSMMASXAXSXSMSXSMSMMMAXAMAMAASAMXMAAAXSAMMXSAMXMXMMSMMAAMSMAMAAMSAMAMMSMMMXMAMMMSMMXAAAXMSAMAMMMMMS
MMSMAMMAMMMAMXMMMXAMXSASAXMASXMXMAAAXAXASXSXMASMMMMMXXAXXAXMAXXMMMMMSMSASASMSSSSXXMAMASAMSSMAAXMXAAMXXSMMXSMXMXAAXMAMASAAAXASMMMXXXMXSMXAAXX
MSAXAMAMMAXAMMMMMSASASASASMMMXSXMSMSMMSXMASAMASASAMASMMAMAMSSSMMXAAMAMXASASMAMMMSMMASXMXSAAXMXMXMSASMMMSAAXMSMSSSMXASMMMSSXMASAMMMXMAXXSXSSM
MSASXSMSSSSMSAAMASXMASAXXAAXASAMMAXXAASXSMSAMASXMAXAXAXMASXMAAXMAMMSXXMAMMMMASASMMSASAAXMMSMMSXXXMXAAAAAMMMAAAXAAASXXMXMAMAXAMXSAAMMASASMMAX
MMAMXMAXAXMASXSMASAMMMAMMXAMXAMXSAMMXMMASASAMXSASXMSMSMXAAAMMMMMXSXMMSMMMXSSMSXSAAMAMMMMMAXAAAASXMXSSMSXMSXMMXMAMXMMXSAXMSMMMSASASMXXMAMXSAM
MMAMXMXMSMMAMXXMMSXSAMXXAXMAMXXAMMSMMAMAMMSAMXSAMXAAAMXMMSXMMSAXAMAAAXAASAAAMMMSMMSMSMXAMSSMMMSMASAMXMXXAMXMSXSAMXMAASXMMAMMMSMXMAXMXXAXMMSS
ASMMXMMMMSMXXSXMASMMXMXMMXMAMSMMSAAMSSMAXXXXMAMAMMMMSMASAMAXAXMMMSSMSSSMSMSAMAAMAMAAAAMSMMAMXXAMXMMMAMAMSAMASAMXSAMMXSAMMASAAMXMXMAXMSMSAAAS
XMXSAAXXAXXAMMAMASASAMXMAASAMXMSAMXMAASXSSMAMASMMMAMMMMMASMMMSMMMAXMAMAAXMMASMSSMMMMMSMXASXMMMSSMXXMAMXMXAAAMAMAXXMAMSAXSASMMXAXXSAAXAMXMMSS
MAAMMMMMMSMXXMAMXMAMSAAMMMXASAMSAMXMMMXMAXSXSAMXAMAMMAXMMMAMAAMAMMMMASMMMXSAMAMAXXXXXMASAMXAXAXAMSXSASMSSXMASMMSXMMAMMAMMAMASASMXMSXMASXXMAM
MMMXMAAAMXMAASMMSMXMXSSSSMSXMAXSAMSSSMMXMMSXMASXMSXSMMMSMMAMSSSSXSASXSMMSAMAMMSAMSAASMMMSSXMMXSAMMASASMAMASMMMAAASMSMMXMMMMMMAMAXMXXSAMAMMMS
XXMASMSXSAMMXAXAAMXSXAXAAMSASXMSAMAAXAASXAMXMAMAAAXSMXAAASXMMMAAAXAXXMAXMAMAMXMMXXXMSAXMASAMXMSAMMAMMMMASAMAAMMMSMAXXXMAAXMXMXMXXXAAMSMMAAMA
XMMMXAAAMMMXMXMSXSAAMXMMMMSAMXXSAMMSMMSAMMSMMASMMMXMAMSSMAMSSMMMSMSMSSSMSAMASXAMSSMXSMMMAXMSMASAMMXSAASXMMSMMMMXMMXMSMASMXSAMMSMMMSSMMSASMSA
MAAMMSMMMMASMAAMAMMSMSMSXXMAMMMMSMAMASAMXMAXSASMXSMMMMAAMMAAAASAMXAAXAAAMXXAMMXMAAAAMMMMMSAAXMXMXMAXMMSMSMSAMXSMMMAMAXMXAAMASAAAAMAXAAXMXMAM
SSXMAAXSXXAASMSMAMSAXXAAXXXXAXXAAMASXMMXSMSXMASMASMMXMAMMXMSSMMASXMSMSSMSMSSSSMXMMXMSAAAMAMASMMMAMMXSAMXAAMXMMXASMMSSSMMMMSSMXSSSMASMMMXMXAM
MASMXSMSAMMXXMMMSMSMAMAMSSMSMSMSMSXSMXSAMAXXMSMMAXASMMMMSMMXAASMMMXXAMAAAAAAAAASXSAMXMXMXAMXAAASMSASMAMSMSMAXSMMMAXAMAAXXXXXAAMAMMAMAMMSSMSA
MAMMAMMMAXSASMSAXAXXXSAMXAAAAAAMASXMAAAAMAMAXXAMMSSMMAAAAAMSMMXMAMAMXMMSMSMMMMXXAXMSSSSMXSXSXSMSASXSMSMXSAMXSXAMSMMMXSAMXSMMMMMMMMMSMMAAMAAM
MASMMSASMMAAAXMASASMXSASMMSMSMSMAMAMSMXSMMXXMSSMMXMASMMSMMXAMSMSSMMSAMXMAMXMXSSMMXSAMXAAAMMMAXAMAMASAMSMXMMMMXMMAXXAXXSMMAMXMASASAMAXMMSSSMX
MASAAMXMMAMAMXMXMAMXXSMMMXMAMMAMASAMXXAMMMSAMAXXMMXAMMAMAMMAMSAAXASXMXMMXMXMAMXAMXMASXMMAXAMAMMMXMAMAXMMASAAXAMMMMMSSMAMSASMSASMSAXAXXAMMXXS
MAMXMXSAMSXSXXXAMXMXXMMXXXMAMSXSASMMMMXSAASAMAMMMMSMMMAMMMSAMMMMSMMSSXSAAMAMASMSMXSAMXXMASMMSSXMSMSSMMXSASMMMASMAMAMAMMMSASAMAMXXXMSMMXSAMMM
MMSMXXSASAAXMMSMSMMMSAASXXMXMAXMMXXAAMMMMMMXMASAAAAAAMASMAMAMXMASAMAMMMSMSASAXMAXMMASXXMAXXAXMASAAAMAAMMASAMSAMXAMASMMXXMAMMMSMSXMXMAMXXMAAX
SAAXMASXMMMMMAAAAASASXMSMXSAMSSSMAXSXMASXMSSSMSMSSSXMSASMSMSMXSXSMMASAAAXMAMXMMXMXSAMXMMSMMMMXMAMXMSMMAMXMAMMASXXSAXMMXSMMMXAMAMMXAXAXMASMSX
MSSXSMMASAAAMSSSMSMASMMXXASXSAAAMMXMMSMSAAAAAASAMXMMAMXXMXAXXAMMSASXSMMSMMAMMMSAMAMMSMMAMAAXAMMXXMAXAXSAMMAMMXMXMMMMSXAXAMXMASAMAMSSSMMMMMMM
XAXXSASAMSSMXAMXMAMXMAAAMXSSMMSMXSAMXMASMMMMMMMXMASMSMSMAMAMMASASXMAXAAAASAMAMMAMSXMAAMASXMMSSXSASXMAXXAXSMSMAMXMASAMMSSMMXSASAMMSAAMXMAAAAA
MSMMSAMXXAMXMMSAMXSXSMMXSAMASXXXAMASMMXMSASMSMSXMAMXXAAMXMAMXXMXSXMASMMSMMAMMMXAXXMSSSMAMAAXAAXSAMXXSAMMMSAAXXSASAMAMXMAAAAMMMMMXSMMMASMSMSS
AAAMXXSSMASAMXMMSMMXMSMAMASAMMXMMSXMASAAXXSAMASAMMSSMSMSXMXMSMMMXXMXXMXXMSXMASXMMXAXAMMSSSMMMSMMAMXMMXMAAMSAMXMASXSSMASXMMSSSSXXAMXXSXXXAAAX
SXSMSXMASAMMAXMMAAMAMAMASAMMAMMXXSASXSMSMMMMMAMAAAAMAAXXXXASAAXMAXXMASXSXMAMASASMMMMAMAAMXMXXAXSAMMXMAAMXXMXXXXAMXAASMSMXSAAAAAASAMMSXMSMMMS
MSMXMASXMXXXMSAXSXSASASXMXSSMXAMMSASAXMAMMAAMAMXMMMSSMSSMSXSXSAMSXMAMXMMASAMXSAASAXSAMXSXSXSSMXSASXMMMSMMXXMAMXMMAXAMXXMSMMXMMMMMASASAXMASMS
SAXMXAMXMSXSASMAMASXSASAMXMAXMXXAMMMMMSAXMXMSMSSMSXAXXAMAAAMAXAMMAMSMSASAMAMXMMMASASASXMAMMMASAXMSASAAXMMSSMSMSMASMMMSAXMASXSXMXSAMASAMMMSAM
MMMSMAXSAMAMAMXAMAMMMMMMXSSSMSMMMMAAAAMASMXXAAAAAAMMSMSXSMSMSMSXMAMMAMXMXSAMAMAXMMXMMMMMAMASAMMMMSAMMMMAAMXAAAAXAMAAAXXXSMMAMAMAMAMXMXMAMSAX
XXASXSMSAMXMMMSSMAMAAAAXMMAAAAAMSMSXSSMXMAASMSMMMMSAMAXAXAAAMAMMSXSMAMAXMSASMSSSXSAXAAXXAMXMMMMAMMXMAMSMMSMMMSMSXSSMMXSMASMASAMASXMAMAXAMSSM
MMMSAMAMAMXMXAAAMXSSXSMMXMMMSMXMMAXXMXMAMXMMAMXMXAXAMSMSMAMXMAMAXMXMAMMSASAMXAAXAXAMSXSSSSXSAASXXMXSXMAAMXMAXMAMXAMAMAAXXMSAXMSXMXSAMAXSMMXM
ASMSMMSSSMASMMSXSXAAAMMSMMSAXMMMMAMAMAXXMMXXXSAMMXSXMXAMXXMASXSMMAMMMAAMXSAXMASMSMSMXAAAAXAMMXXMASAMXXXSMASMSMMMAMSAMSXMSMMMSMXASMSAMSMMAMSS
SMAMXSXAMMASAXAASMMMXMAAAMMAMXAXMASXMMXSMMSSMMAMMMMAMMSMMMSXSXMASMSAMMXSAMXSXAAXMAMAMMMMMMMMMSMSAMASAMSXMXXMAAAXMXMMMMAMXAASAXXAXAMMMMASXMAS
MMAAXAMMMXMSMMMSMAMSMMSMSSMAMSSMMXXMASAAAAAASMXMAAAAXAAXAXAMXXMAAASMSSMMASMMMMSMMMMAMAXAMXMAXAMMASXMASMAXMXSSMMMXSMXASAMMSMSASMAMXMXAXMMSMXS
XSXSMMMAAAXMMSSMMSMAXXAXXAMXXAXAXMAMAMSSMMMAMXMSSXXSMSMSSXMMMXMMMMMAAXASASAXAXAXAMMXSMXMSSSSSMXMAMXXSAMMMMAMAAXXAXAMXMAMXXAMAMXXSAMMMSAAMMAM
MAMXAXSMSXSAAXAXAMSMMMMSAMXSMASMMSAMSXMXXXMSMXMMASXXMXXAMSMAMASMXMMMMXMMASMMSSMSASXXMAXMAMMXAXMXSSMMXXXMAMASXMMMSSSMSSSMAMAMAXMAXAMASAMXMMXS
XMASMMMAAAMMMSAMMXSXMXAAMXAAMXMMASAXMAMMMXMMASAMAMMAAMMASASXSASMAAXASMSMXMXAAAXMAMMAMXSMASMMSMSAMAASXSXSAMXMXAAXMAAAMAMMMSSMMXAMXSMXXXAAXXAA
MMMXMSMMMSMAXXAXMAMAMMMSSMSMSMSMAMXMSSMMMAAMAMMMMSSMMXSMSXSXMAMXASXXMAMXMXMMMXXMAMSXMAXXAMXAAAMMSMMMAMASMSSMSMMSMMMMMMMAAXAAMXSMAXXSMASMSMSS
MASAMSAMXAMSMSAMMMSAMASAXAAXMAXMSSMMAMAASMMMSMXAAXXXMXAASAMXMAMASMMSMAMSAMMSMSAXSAMXMXSMMMXSMSMXSAMMXMAMXAAXMXMXXMAAXXMMXSXMMSMMMSAAMAXAAAAX
SAXAXSMMSAMXAMAXMASASXSXMMMSMSMXMAXSAMMMXAAAMASMSMSAMSSMMMXXMMMMXAASMMMXSXAAASMMMAMXSAMXMAMXXXAASAMAAMXSMSMMMSMAMMSMSMMSASXMXSAAXMXMSMMXMMMM
MMXSMMXMAMMMSMSMMASXMXMASMMMAAAAXXMMASMXSXMMSAXXAASXXAAAASMSXSAXSMMSASXMMMXMMMAMSSMMXXMASMXSAMXXSAMMMSAMMXAXAAMASAMAXAXMASASMSSMSAAMAXSSSMSX
XAAXAMASXMAAAXMAMASAAXMAMAASMSSSSXXSAMXMXAXMMMMSSMMXMSSMMSAAASMXMMSXMMAAXAMMSASXAAAMAMXMAXAXMMSAMMSAAXMSASAMSMSMSAXSSSSMAMAXAXXXSMMSAASAAAMX
MMMSASASAMMSSXSAMXSMXSMSMSMXAXAAXXMMMSXMSSMAAAMXMAMAMMMXMMMMMMXSXXAMSXSMMMMXMAMMXXMMAMAMAMAMXXMASASMSMSMMMXAXMAXMXMXXAAMAXMMSMMMMAXMMMMSMMMA
MSASMMMXMXAAMXSAXXXXAMAMAXAMSMMMMSASASAMAXMSMSXAXASXSMSXMASMXMAMXMSASAXAAMMAMAMXSSXSASASMXASMMSMMASAXXSAXXSSSSSSSXSXMXMAMAMXXAAAMXSMMXXMSMXS
SMMMMMMMSMMSXMSXMSAMMSAMSMXMXAAAASAMASMMMSAMXMXSMMSMAXSASASASMAXXXMAMAMMMASMSXAAASASXXMAXMMMMASAMXMMMASMMXXAMAMXAAAMAAXAMSAMMXSSSMXMAXSAMXAX
SAMSMSAAXAAMAMXAXSAMXMXSXASXXMMXXMAMAMAAASXSASAMAMXMAMSAMXSAXSXMSAMAMAMASXSAMXMXMMMMMMMMSMSAMMSAMMASMXMAXXXMMMMMMMMASASXMXAMXAMAMAXXAMMXMMSS
SAMAASMMSMASAMSSMMXSMMMAMMMMXSSSXSAMXSMMMSASXMASMSSXMAMAMAMXMMMMMXSASXMAXXXAMXMMXAAAAXAMMAMXSAXASXAXMASXMMMXXASMAMXMMMMAMMAMMXMAMSMMMSMAXAMA
SAMMXMAMXMAMAMAXAMAXAXMAAAAXSAAMASXSMMMMAMMMMMMMXAXAXMAMMXSSMSAAAXSASXMSSSSMMXMAXXXSSSMSMMMSMMSAMMXXMMMMAAMMSMMSAXSMSASAMSSMMAMAMAXAAAMAMSSM
XAMSASAMXMASASMSXMASXMXMXSXSMMAMAMXXAAAMAMSASAAAXMSMMSSMXXMAAMSMSXMAMXAXAMXMAMXSSSMAXAAAMXXXAMMAMMMMXAAMMSAAASMMMSXASASAXXMAXSSMSXSMSSMMXMAX
SSMSASMMMXMAAXXSAMXSAAMSMXXXAASMSSXSXMSSSXSASMMXAXAMXAAMXAMMMMMXXXMAMMAMXMMMAMXAAAAMMMSMSSMMXMSAAASXSSMSAMMSMSMMMAMMMAMXMXXSMAAAAXMAXMAXXSAM
XAAMAMMSSMSMXMAMSAMXMSAAASMSXMXAXXXSAMXAXMMXMAXSMXSSMSSMMASXAXXAMMSMXMAMMAASASXMSMMXAXAAXMASAMXSMAAAAAAMMMMXASMSMMAXMAMASXAMMXMMMMXMSSMMXMAS
SMMMMMXXAAXXAMMSASAMXMXMSMAAMMMMMSAMXSMMMXMMMMMASMMXXMAMXAMXMMMXMAAMASASMSMMASMXMAXSSSSXMSAMASXXSSMMMMMMMAAMXMAAAXSXSSSMSMXSAMXMAAAXMAMSMMAM
SAMXMSXSMMMSXXSAMXXXXMXXXAXXAXAMAMMSMAMXSAASAMXAMMSMXSASXXMASAAXMSMXAMAMAMXMMMMAMSMAMMXAXMMSAMXAMMAXXXSSSMSMSMSMSXXMMASXXAMXMXMSMSXXSAMASXAS
SAMSSSMXXAXAXMXMASXMSMASMMMSSSMSXMAAMXXAMMSMAXMASXAAAMASMXAXXXSXMASMXSAMAMXMAAMAMMAXSASXMAXMMSMXMSMXSAAAMMMMMAXAXMSASAMXMMMMAAXXAMXXMASASXMM
SMMXAMMMMMXSXSAXXXAAAXMXAAXAAMXAMMSMSMMXSXMXAMXSMMMSMMXMAAMMSAXXSAMXAAXSXSSSSSSXSAXXMASXXXMAXMASAAMAMMMMMASAMSMAMASXMASMMMAASXSSSXSMSXMASAMX
SMMSXMASASMMASMSMSMSMSMSSMMMMMMSSMAAAAMAMAMMMSXAAXXMAMMMXXAAMXAAMASMMMMSMMAAMAAMXMAMMMMAMSSSMSAMAAMASAAXSAXAMAMXMXMAMSMMAAMMXXAMXAMXAXXASMMA
XAASASXMMMAMXMAAXAAXXAXAMXXMASXMAXXSSSMASAMAAMMMMMXSAMMMAMMXSMMMSXMAMAAXAXMMMMMMSSMSAMMAMMAXAMXSXXSASXSMMMSSMMMMMMMMXXASMXSAXMMMMSMMMMSAMAAA
SMMSAMAMSMXMAMXMXMAMXMASMSMSAMASMMMMMMMMXXSMXSAMMSAXASAXSMXAAXXXXAMAMMSSSMAASAAXMAXMAMSSXMAMSMMXMASAXXMASAAXAXMAAAXXMSAMAXMASAXMXMASAAMAMSMS
AAAMAMSMSAASXSAAMXSXXMAMAMMMMSMSASASASMXSASXAMAASMSSMMMXMAASMMSSMMMSXMMAMASMSSSSMMMSSMMXAMAMAAXXMXMXMXXAMMXXXMSSSSSXMMMMAMXSXXXMAXMMMXXAMAAX
SMMSAMAAXSMMASMSMAXASXAMAMXAXAASASASASAAMAMMSSMMMAXXAASXMMMXAMMMASAXAMMXMAMXXXXMMXAAMAXMMSASXSMMMAMXSSMSMSASAXAAXXXMSAMSMSMMAMMMSMAMAMSSSMSM
AAXSXSMMMAMXMXAMMXMASXXSSXXASMMMAMMMMMMMMAMAXXMAMSMXMASXAXSSXMASAMAXAMSAMXSXMXMSXMXSSSMSAAMSAMAMSMSAXAAAAASAAMMMMMXAMAXAAAAMSMAAAXAMMMAMAXAA
MSMMXMXXMXMAMMMMMAMMMMMAMAAXMMXMXMXAXXXMSMMMSAMXSAAXMSXXXMMAMSASAMASXMSASAAMMAMASMMMAMXMMSSMAMSMAAMXMMMMSMAMAXAAAAASXMMMSMXMXSMSSMXSSMXXMMMS
XXASASXMXAMMXAAMMASAAMMAMXMAAXXSAMSASMSAMAXMMAMXSASMXMAMXXMSMMAXXMASMASAMMSMXAXXSMAMAMMSMMAXXMMMXSASXSAMMMMXMSSSMSMMXASXXMSMXMMAXMMXMXMASXXM
MSAXAXAXMSMAXSSMSASMSXSSSMMSMMMSAMXMXMXASMMSMMSMSMMMXMXMAMMAAMAMXAMXMAMAMXAMSXSAMASMSMMAMMAMXXXMXAAMMSASAAXAMAMXMMMSSXMASAAMAAMMSMSASASAMAAM
MMMMSMMMAMMSMAAAMXSXMXXMAXAXAAASMMAXMSSXMXAMSAAASAAAAXMSAMSAMMAXXAMXMMSSMMMXAMMAMAMMAAXAXSMSXSMSXMAMASXMXSSXASXSXSAAAAMAMMMSSSMXAXMAMAMMMSAM
MSMAMAASMSAMMMMXMASXMAMXMMMSSMXSASXMAMMMAMSMXSMMMSMSMSAXSMXAXSASXMSAAAAAMMXMASAMXASXMSMAXSAXAXAAMXXMAXXMAMMMMMAAAMMMSMMXSSXXAAMMXXMSMSMSXMAS
AAMMSMXSXMAMXMASMMXXAAXSXMXAAMASXMAASAAAMAMXMASAXXMAAMMMMXMMMMASAAXXMMSSMMXSMMMMSMXXAMXSAMXMSMSMSSSMSXMMAXAAXMMMMMXXMAXAMMXMSMMMSMXMAMAAASMM
SMXXAAAMAXAMXXAXAAXMMXSXAMMSSMASMAAMASXSXXAMSASXSXMMMMASXAMAAMMMMXMXXMAMAXAXXAAXAMMMSMAMXAAXAAAAXXAMMASXSSSSSXXAXXMMSSMSXSXMASAAXMAMAMXMAMXA
AAASMSXMAMSAMXXMAMXAXMMMMMXAXMMXAXMXXMMMMXAXMASAAMXMMMASXXMASXSXXMAMAMAXMMMSSSSSMSAAMXAMSSXMMSMSMSMMSXMAMXMAXMSXSXMAXMXMAMXSASMSAMMSMMAXMMSX
MAMXAXMASXXASASXSMSSXMAAXAMXXSAMSXMAMMAAMMSMMXMXMASMSMASASXAMASMASASXSMSAAXXAAXXAMMMMMAMAMXAMAMAAAMASASXSAMAMMMAMAMMXSAMXMMMASXXAMAAAXMSAAMA
SSSMSMSAMAXAMASXXAAAAMSSMMSMXMMSMAXSMSMMSAAXXXAMXMXAAMXMAMMXMAMSXMAXMAAXMMSMMSMSSMSASMXMASMXMASMSMMASASAMAMMMAMXMAXSMXAXXMAXAMASXMSMXMAMMMSX
AAAAXAMXSMMSMMMMMMMSXMMMMMAAAMXAMMMXAAAXMMSMMMSMXMMSMSASAXXXMXMXXMSSMMMXSXAMAAAMAASASXAMSMMMSXMXAXMMSAMMMAMXSXSSXSAAASXMSMXMASMXMAMASMSMXMAA
MSMMMMMXMAMMAAXAAMXXAXAAASMXMSSMMSASXSSMMSAAMAAAASAXXXXMXSASXSMXXAAAXXMASXMMXSSSMMMXMASXAAAXAMSMMMSAMMMXSASMSMAXAMSMMMSXAAASAMXMMAMMSAAXSMSM
XMXXMAMXXXSXSMSSXMASMXMSMSXXSXXAAAMAAAMAXSXSMSMMXMASMSXXAAAXMASAMMSSMMMMMXXMAXXAXSXAASXSMSMSAMXAAAMASASMSASAXMAMXMASAAXSMSMMAMXASXSAMXMMMAAX
MSMSSSMMSMAAXXMASMAMAAXMMMXXXAMMMMMMMMMMMSXMMXXMAMSMAAXSMMSMMSAMXAAMMMASXSMSXXAXAMSXSAAMXAAXXMSMMMSSMMXAMMMMMMXXAMAXMMXXXMASXMSMXMMMSMXSMSMS
AAAXAXXAAMMMXAMAMMAMMMSAAAXSMMMSAXXAMAXSAMAXMAXXAMXMMMMXAAXXSAMXXMMSMSMSASASAASMSASMMMSMSMXMAASXSMMMAXMSMMAMXMMXSMXXAXSASAMXAAXSASMXAAAMAMAS
XMSMXMMSXSXMXMMMMSMSXXXMMSXMAMAMXSXMSASMAMXMMAMSSSXSAXSMMMSMMAMASMXSAAMMMMXMSMXAMAMAXAMAMXASAMXAMASXXMAXMXMSSSMAAAASMMMASXSSMMMSXMXMMMMAAMMM
SSMAAAXMXSAMXSAMASAMMSMMXXASAMXSASAXMMSXSMMAMAXXAMASMMMAAAAASXMAXXAMSMSSSXSAMXMAMASXMASAMSMSAAXMSAMXAXSXSAMXAAMAMMMAAMMAMMXAMMAMAMAXXASXMSSS
XMASXSMMXSAMMSASAMAAAMAMAMMXAXAMAMSSSSXAMAMSMMSMAMAMMASXMXSMMAMXSMXMAMAAAMXMMXMXSAMMMMSAMXAMMMMXMASXMAMAMXSMMMMXXASMMMMMSAMXMMASASASMXXAMXAS
MMAMMMASASAMAXAMASMMXSAMXSMSSMSMSMAMXAMXMAMXAAXXAMASMASAAAMMSXMAXXMMSSMMMAXSAMXAMASASAXXMMMMAAXMSMMMMMSAMXXMASXMSXSAMXMMMXMAMXASASASXMXSMMMM
AMASASXMASAMMSSSMMMMMSXSMMAAXMAAAMAMMSMMSSSSMMMSMSASMASMMMSASXSMSMXAXXXXXSMAXXMMXMMAMASXMAXMSXSXMASXSASASXASMSAMAMSAMXSAMMSASMMMMMXMMSAMXSAM
MMASASXMAMXMMAMXMAASMMXMAMMSSXMMMSASXAAXAAXXAAAXXMXSMAXAMXMAMAXAAAMSSMSAMXAXMSXSAMMSMXAAMSSMASAAMXAAMASAMMMMMSXMAASAMAMASMMMXMXAAMXXAMASXSAS
MSMMMMXMXMAXMAXXSSMSAMXMAMXAXXXAAMAMXSMMMSXSSMSAXMXXMXMSMXMSMXMMMSMMAMSAXXMXASASASAXMMSMMAAAMAMMSAMXMXMMMSAAMXASMMSAMAMXXXAMMMSSMSMSAMAMXSAM
MAAAAMAXMMAMSSMAMAMSAMASMSMSSMSMMSASAAAXAXMMXAMXMASMXXXMASAAAASMAMMSSMMMSMMSAMAMSMXSSXXAMSMMXMAAXAXXXXAAAXSMMXXXMAMMMSAAMSMXAAMAXXAMXMMXMMMM
SSSMSXSSXMXMAAAMXSASMMMSAAMMAMXAXSXMXSMMMMAASXMAMXMXXMASAMAMSMMASXMAMAASAAASAMXMAXXAXASMMXAAXXMSSMSSMSSMSMMMSSSSMMSXAAMXMAAMXSMMMMXMAMMAMAMX
XAAAAAXAMMXMXSMAMXAXXXAMMMMSAMMXMSMMAXXASXMMSASXMSMASMAMAMXXXAMAMAMXSSMSMSMSAMXSSMMAMMMAASXMMXAMAXAAXAXAMXXSAAMMAAAMXSMSMMXXAAXMAAMSXSAMSASM
XSAMMXMASXMAXXXMAMMMMMMMAMMSASXMAMAMASMMMAXXMAMMAAMXSMXMAMSSSMMXSXMAXMASMMMSAMXAAASMMXSMMXXAMXMSXMSXMMSMASXMMSMSMMSSXAASMAAMXMMSMSXXAMAXSAMA
MXMASXMMMASMMMSXSAASMXSSXMMSAXMAXSAMXSAASXMSMMMMSMSAXMSMMMAAAMSMMAAMXMASXAASMMMMMMAAAXMASXMAMXXMMMMMMXAMXASXAAAAAXAXMMAMMMSMSAXSAMMMMMSMSMSM
MAMAXMAMXXMASMSAMSSSXAMASAAMMMMSMSXSMSMMMMAAAASMAAMMSAAAAMMMMMAASASMSMASXMXMSAAXXMMXMMSAMMSAMXXSASAAMAXSAMXMSSSSSMMSMMMSASAAXMMMXMXXMAMXXAAX
XXSMMSMMSASXXAMAMXMMMMSAXMXMXASAXXMAMXAXSXSSSMMSXXSXSXSMMSXASMSMMAMAMMAMXMAMSSSSXXXXSAMAMXSASMXXXSMSSMXMAXXMMMXXMASXXAASMSMAMSASAMMMMSSSMSMS
XMAMAAAASXSMSSMMMSAAAMMMMXAMMXMMSSSMMMMMMAMAAAMMSXSAMAXAMXXXSAMAMMMAMMMMXMAMMAMAXXASMXSSMASMMMMMXMAXAXAXAMXMAMSXSSMSSMXSXMASMSASMSAAMXAAAAMX
XMAASMMMSAMAAXAXASMSMXAAAMAXMAMSXMAXMAMAMAMSMMAAMXMMMAMXMAMMMAMAXSSXSASASMSSMAMAMMMMAAAXMXMXSAASASXXASXSMMXSASMAMXAMXMAMASMMAMAMASMSSMMMSXSX
XMAMMAMSMAMMMSMMXXAXXSMSXSAASAMXASMMSMSASAXXAXMAMAMAMXSSMASXMMMXMMAASASAMAAAMAMAMXXXMMSMSMMAMSMSASAMXMMAAXASXMMAMMMMAMASMMXMMMAMXMAMXMSXAMSX
XXXXXMMASAMXXSXXXMSMMMAAAMXMXAMSMMXMAASXSMSMMMSAMMSASAAXSAXMXXSXSMAMMXMAMXMASXSAMXXAXMXAAAMXXMXMMMMMMASXMSMSSXSASAASMSASAXXMXSMSSMXMASAMXSMA
XXAMXXSXSMMXXMAMXMAAXMXMMAMMSAMAAAXSMXSAXAMXSASASAAMSMSXMXMMSAXASMXSMXSXMMSAMXSMSMSXMSSSSSMXMASXSAMXSMMAAMXMAMSAXAMMAMASMMMSAXSAAMSSMMMAMAMX
SSMMXXAMMMXMXMAMMMSSMASMXSAXMASMMMMXXAMXMSAXMASAMXSMXAMXXMSAAMMMMXMAMAMASMMSMMSAAASAMAAXMAXXSXSASMSMMAMMAMSSMMMMSXSMSMAMAAMMASMSMSAMMAXAXAMX
MAMSMMMMASAMASASXAAAMASMAMMSAMXAASMMMMSAMXAXMAMXMAXXMSMMSAMXSMSASXSAMXSAMAAXMAMSMMSAMXSMMXMMAMMAMXAMSSMMSMAAAXMASAAAXMSMSSSMXMAXMMASMSSMSSSM
MMMAAAXSASASASMSXMSSMASMXMXMASMSMMAAAAXXAASMSAMXMSSXMAAXMAMAAASASASXSAMXSMMSMMXXXXSAMAXAXAXAAMMAMSMXAMSAAMSSMMSAMSMMMMAAMAXMMSAXXMAMAAAAAMXA
SXSSSMXMASXMXSXMAMXAMXSAMXXXSXXMXSSMMSAXSAMAXXMXMMSXSMSMSAMSSXMXMAMSMXSAXMSXXXMXAMSMMXSSMSMSASMMMXSMXSMSSMMAMXMAXAMXSSMSMSMMMMMSMMASMSMMMSAS
"""

# Convert the multiline string into a list of strings (grid)
grid = [line.strip() for line in input_string.strip().split('\n') if line.strip()]

# Count the occurrences of the X-MAS pattern and get the found patterns
count, found_patterns = count_x_mas_occurrences(grid)

# Print the result
print(f"The X-MAS pattern appears {count} times in the grid.")