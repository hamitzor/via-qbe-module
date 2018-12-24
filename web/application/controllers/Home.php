<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Home extends CI_Controller
{
  public function index()
  {
    $this->smartyci->display('index.tpl');
  }

  public function search()
  {
    $id = $this->input->get('id');

    $model['name'] = 'Video - ' . $id;
    $model['id'] = $id;

    $this->smartyci->assign('model', $model);
    $this->smartyci->display('search.tpl');
  }

  public function search_submit()
  {
    $id = $this->input->post('id');

    $model['name'] = 'Video - ' . $id;
    $model['id'] = $id;

    $target_dir = FCPATH . "uploads/";
    $name = $_FILES["example"]["name"];
    $explode = (explode(".", $name));
    $ext = end($explode);
    $target_file = $target_dir . uniqid() . '.' . $ext;

    if (move_uploaded_file($_FILES["example"]["tmp_name"], $target_file)) {
      $this->smartyci->assign('model', $model);
      $this->smartyci->display('search-result.tpl');
    } else {
      $this->smartyci->display('search-error.tpl');
    }
  }
}
