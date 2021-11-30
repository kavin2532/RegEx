    import psycopg

    CONNECT_ARGS = 'host=localhost user=postgres1 password=mypassword dbname=test'

    def exportPlants(outfileName):
        outfile = file(outfileName, 'w')
        connection = psycopg.connect(CONNECT_ARGS)
        cursor = connection.cursor()
        cursor.execute("select * from Plant_DB order by p_name")
        rows = cursor.fetchall()
        outfile.write('<?xml version="1.0" ?>\n')
        outfile.write('<mydata>\n')
        for row in rows:
            outfile.write('  <row>\n')
            outfile.write('    <name>%s</name>\n' % row[0])
            outfile.write('    <desc>%s</desc>\n' % row[1])
            outfile.write('    <rating>%s</rating>\n' % row[2])
            outfile.write('  </row>\n')
        outfile.write('</mydata>\n')
        outfile.close()

And, here is sample output:

    <?xml version="1.0" ?>
    <mydata>
      <row>
        <name>almonds</name>
        <desc>good nuts</desc>
        <rating>4</rating>
      </row>
      <row>
        <name>apricot</name>
        <desc>sweet fruit</desc>
        <rating>4</rating>
      </row>
      <row>
        <name>arugula</name>
        <desc>heavy taste</desc>
        <rating>4</rating>
      </row>
      <row>
        <name>chard</name>
        <desc>leafy green</desc>
        <rating>4</rating>
      </row>
    </mydata>

