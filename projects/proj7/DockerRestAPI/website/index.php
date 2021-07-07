<html>
    <head>
        <title>CIS 322 REST-api demo: Laptop list</title>
    </head>

    <body>
        <h1>List of laptops</h1>
        <ul>
            <?php
            /*
            $json = file_get_contents('http://laptop-service/');
            $obj = json_decode($json);
	          $laptops = $obj->Laptops;
            foreach ($laptops as $l) {
                echo "<li>$l</li>";
            }*/
                #
                #Add all url
                #List all
                $json = file_get_contents('http://laptop-service:5000/listAll');
                $obj = json_decode($json);
                    $Opentime = $obj->Opentime;
                    $Closetime = $obj ->Closetime;
                foreach ($Opentime as $o){
                    echo "<li>$o</li>";
                }
                foreach ($Closetime as $o){
                    echo "<li>$o</li>";
                }
            
                #List all, opentime only
                $json = file_get_contents('http://laptop-service:5000/listOpenOnly');
                $obj = json_decode($json);
                    $Opentime = $obj->Opentime;
                foreach ($Opentime as $o){
                    echo "<li>$o</li>";
                }
                $json = file_get_contents('http://laptop-service:5000/listOpenOnly/json');
                $obj = json_decode($json);
                $Opentime = $obj->Opentime;
                foreach ($Opentime as $o){
                    echo "<li>$o</li>";
                }
            
                #List all, close time only
                $json = file_get_contents('http://laptop-service:5000/listCloseOnly');
                $obj = json_decode($json);
                    $Closetime = $obj->Closetime;
                foreach ($Closetime as $o){
                echo "<li>$o</li>";
                }
                $json = file_get_contents('http://laptop-service:5000/listCloseOnly/json');
                $obj = json_decode($json);
                $Closetime = $obj->Closetime;
                foreach ($Closetime as $o){
                    echo "<li>$o</li>";
                }
            
                #
                $json = file_get_contents('http://laptop-service:5000/listAll/json');
                $obj = json_decode($json);
                $Opentime = $obj->Opentime;
                $Closetime = $obj ->Closetime;
                foreach ($Opentime as $o){
                    echo "<li>$o</li>";
                }
                foreach ($Closetime as $o){
                    echo "<li>$o</li>";
                }
            
                $ListClose_csv = file_get_contents('http://laptop-service:5000/listCloseOnly/csv');
                echo $ListClose_csv;
            
                $ListOpen_csv = file_get_contents('http://laptop-service:5000/listOpenOnly/csv');
                echo $ListOpen_csv;
            
                $ListAll_csv = file_get_contents('http://laptop-service:5000/listAll/csv');
                echo $ListAll_csv;
                
            ?>
        </ul>
    </body>
</html>
