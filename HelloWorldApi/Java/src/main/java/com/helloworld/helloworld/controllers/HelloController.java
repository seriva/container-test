  package com.helloworld.helloworld.controllers;

import java.util.List;
import java.util.ArrayList;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.PathVariable;
import com.helloworld.helloworld.models.HelloModel;

@RestController
@RequestMapping("/hello")
class HelloController {
	@GetMapping
    public ResponseEntity<HelloModel> getHelloMessage() {
        return ResponseEntity.ok(new HelloModel("Hello, world!"));
    }
}