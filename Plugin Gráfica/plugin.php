<?php
/*
Plugin Name: Gráfica de IPs maliciosas
Description: Genera una gráfica con las 10 direcciones IP maliciosas con mayor número de conexiones.
Version: 1.0
Author: Grupo 4 - SGCUW
License: GPL2
*/

add_action('admin_menu', 'add_to_menu');

function add_to_menu() {
    $page_title = 'IPs maliciosas';
    $menu_title = 'IPs maliciosas';
    $capability = 'edit_posts';
    $menu_slug = 'plugin_ips_maliciosas';
    $function = 'mostrar_grafica';
    $icon_url = 'dashicons-chart-bar';
    $position = 6;

    add_menu_page ( $page_title, $menu_title, $capability, $menu_slug,
                    $function, $icon_url, $position );

    include 'grafica.php';
}