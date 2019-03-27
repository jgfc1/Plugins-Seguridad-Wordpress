<?php

function mostrar_grafica() {
    $curl = curl_init();

    curl_setopt_array($curl, array(
        CURLOPT_URL => "https://riskdiscovery.com/honeydb/api/bad-hosts",
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_ENCODING => "",
        CURLOPT_MAXREDIRS => 10,
        CURLOPT_TIMEOUT => 0,
        CURLOPT_FOLLOWLOCATION => false,
        CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
        CURLOPT_CUSTOMREQUEST => "GET",
        CURLOPT_HTTPHEADER => array(
            "X-HoneyDb-ApiId: 78873774c1ab986e01ced74af594e06b807a293e19887de8d15d7804cbaaaaaf",
            "X-HoneyDb-ApiKey: 62364c2a2936545a13188db53cf0952d1ece0f0b6fc9bd589a5be19f8be5599b"
        ),
    ));

    $response = curl_exec($curl);
    $err = curl_error($curl);

    curl_close($curl);

    if ($err) {
        echo "cURL Error #:" . $err;
    } else {
        $responseJSON = json_decode($response, true);

        $output = array_slice($responseJSON, 0, 10);
        $nums = array();
        $tags = array();

        foreach ($output as $elem) {
            array_push($nums, $elem['count']);
            array_push($tags, $elem['remote_host']);
        }
        ?>
        
        <script>
            window.onload = function () {
                var nums = <?php echo json_encode($nums); ?>;
                var tags = <?php echo json_encode($tags); ?>;
                var dataPoints = [];

                for (var i = 0; i < 10; i++) {
                    dataPoints.push({
                        y: Number(nums[i]),
                        label: new String(tags[i]),
                    });
                }

                var max = dataPoints[0].y;

                var chart = new CanvasJS.Chart("chartContainer", {
                    animationEnabled: true,
                    theme: "light2",
                    title: { 
                        text: "Conexiones de cada dirección IP maliciosa",
                        fontSize: 20
                    },
                    axisY: { 
                        title: "Nº conexiones",
                        interval: Math.ceil(max * 0.2 / 2000) * 1000
                    },
                    axisX: { title: "Direcciones IP maliciosas" },
                    dataPointWidth: 70,
                        
                    data: [{
                            type: "column",
                            indexLabel: "{y}",
                            indexLabelPlacement: "outside",
                            dataPoints: dataPoints
                    }]
                });
                chart.render();
            }    
        </script>
        
        <?php
        echo '<h1>Top 10 direcciones IP maliciosas</h1>';
        echo '<div id="chartContainer" style="height: 500px;margin-top: 2%;width: 95%;"></div>';
    }
}
?>
<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>