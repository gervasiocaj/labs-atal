import java.io.*;
import java.util.LinkedList;

class Main {
    public static void main (String args[]) {
        Main myWork = new Main();
        myWork.Begin();
    }
    
    static String ReadLn (int maxLg) { // utility function to read from stdin
        byte lin[] = new byte [maxLg];
        int lg = 0, car = -1;

        try {
            while (lg < maxLg) {
                car = System.in.read();
                if ((car < 0) || (car == '\n')) break;
                lin [lg++] += car;
            }
        } catch (IOException e) {
            return (null);
        }

        if ((car < 0) && (lg == 0)) return (null);  // eof
        return (new String (lin, 0, lg-1)); // XXX changed lg to lg-1, so it will read only the character w/o the \n
    }

    void Begin() {
        String input, result;
        int res, n, d;
        boolean includingZeroStart = true;
        
        // size will be of 9*9*8*7*6
        LinkedList<String> numeradores = Main.permutations(!includingZeroStart); //This will be ABCDE, and A is never zero
        LinkedList<String> denominadores = Main.permutations(includingZeroStart); //This will be FGHIJ
        

        while (!(input = Main.ReadLn(255)).equals("0")) {
        	res = Integer.parseInt(input);
        	result = "There are no solutions for " + input + ".";

			for (String numer : numeradores) {
				for (String denom : denominadores) {
					n = Integer.parseInt(numer);
					d = Integer.parseInt(denom);
					if (n/d == res && n%d == 0)
						if (!hasRepeatingChars(numer, denom))
							System.out.println(n + " / " + d + " = " + res);
				}
			}
				
			System.out.println(result);
        	System.out.println();
        }
    }
    
    static boolean hasRepeatingChars(String a, String b) {
    	char[] achars = a.toCharArray();
    	
    	for (int i = 0; i < achars.length; i++) {
    		if (b.indexOf(achars[i]) != -1)
    			return false;
    		if (a.indexOf(achars[i]) != a.lastIndexOf(achars[i]))
    			return false;
		}
		return true;
    }
    
    static LinkedList<String> permutations(boolean includingZeroStart) {
    	LinkedList<String> ps = new LinkedList<String>();
        arranjo("", "0123456789", ps, includingZeroStart);
    	return ps;
    }

    static void arranjo(String prefixo, String str, LinkedList<String> ps, boolean includeZero) { // http://stackoverflow.com/a/4240323s
    	if (!includeZero)
    		if (prefixo.startsWith("0"))
    			return;
		if (prefixo.length() == 5) ps.add(prefixo);
		else
			for (int i = 0; i < str.length(); i++)
				arranjo(
						prefixo + str.charAt(i),
						str.substring(0, i) + str.substring(i + 1, str.length()),
						ps, includeZero);
	}
}
