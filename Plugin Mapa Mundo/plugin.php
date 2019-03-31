<?php
/*
Plugin Name: Mapa
Description: Genera un mapa con la geolocalizacion de las IPs maliciosas extraida de un repositorio de Cyber Threat Intelligence externo
Version: 1.0
Author: Grupo 4 - SGCUW
License: GPL2
*/
add_action('admin_menu', 'add_to_menu_mapa');

function add_to_menu_mapa() {
    $page_title = 'Mapa';
    $menu_title = 'Mapa';
    $capability = 'edit_posts';
    $menu_slug = 'plugin_ips_maliciosas_mapa';
    $function = 'mostrar_mapa';
    $icon_url = 'dashicons-admin-site';
    $position = 7;

    add_menu_page ( $page_title, $menu_title, $capability, $menu_slug,
                    $function, $icon_url, $position );

    include 'loadMap.php';
}
