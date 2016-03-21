<?php

class Human
{

    private $name = "name";

    private $age = 23;

    /**
     *
     * @return the $age
     */
    public function getAge()
    {
        return $this->age;
    }

    /**
     *
     * @param number $age            
     */
    public function setAge($age)
    {
        $this->age = $age;
    }

    /**
     * ssssssssssssss
     */
    public function eat()
    {
        echo "eating\n";
    }

    /**
     *
     * @return the $name
     */
    public function getName()
    {
        return $this->name;
    }

    /**
     *
     * @param string $name            
     */
    public function setName($name)
    {
        $this->name = $name;
    }
}