zip -r ../excalibot.zip * &&
echo '#!/usr/bin/env python3' | cat - ../excalibot.zip > excalibot &&
chmod +x excalibot &&
rm ../excalibot.zip