<?php

if (!defined('BASEPATH'))
{
  exit('No direct script access allowed');
}

require_once('application/third_party/smarty-3.1.32/libs/Smarty.class.php');


class Smartyci extends Smarty
{
  public function __construct()
  {
    parent::__construct();

    //$this->caching = 1;
    $this->setTemplateDir(APPPATH . 'views');
    $this->setCompileDir(APPPATH . 'third_party/smarty-3.1.32/templates_c');
    $this->setConfigDir(APPPATH . 'third_party/smarty-3.1.32/configs');
    //$this->setCacheDir( $config['application_dir'] . 'cache' );
    $this->right_delimiter = '}}';
    $this->left_delimiter = '{{';
  }

  //if specified template is cached then display template and exit, otherwise, do nothing.
  public function useCached($tpl, $cacheId = null)
  {
    if ($this->isCached($tpl, $cacheId))
    {
      $this->display($tpl, $cacheId);
      exit();
    }
  }
}